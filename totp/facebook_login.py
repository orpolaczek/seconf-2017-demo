from selenium import webdriver
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time
import pyotp
from private_passwords import FacebookAuth

class FBSanityTest(unittest.TestCase):

    def get_incognito_caps(self):
        options = Options()
        options.add_argument("-incognito")
        options.add_argument("--disable-popup-blocking")
        return options

    def setUp(self):
        self.driver = webdriver.Chrome('/usr/local/bin/chromedriver',
                                       chrome_options=self.get_incognito_caps())
        self.totp = pyotp.TOTP(FacebookAuth.AUTHENTICATOR_KEY)
    def tearDown(self):
        self.driver.quit()

    def observe_until_elm_cls_appear(self, class_name, timeout=10):
        print("Observing for class={}".format(class_name))
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, class_name)))

    def observe_until_elm_id_appear(self, id_name, timeout=10):
        print("Observing for id={}".format(id_name))
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.presence_of_element_located((By.ID, id_name)))


    def test_login_with_otp(self):
        driver = self.driver

        # Open FB
        driver.get("http://www.facebook.com")
        self.observe_until_elm_id_appear("login_form", 5)

        # Enter user & pass
        email_elm = driver.find_element_by_id("email")
        if email_elm:
            email_elm.send_keys(FacebookAuth.USERNAME)

        password_elm = driver.find_element_by_id("pass")
        if password_elm:
            password_elm.send_keys(FacebookAuth.PASSWORD)

        time.sleep(2)
        # Press login
        login_elm = driver.find_element_by_id("loginbutton")
        if login_elm:
            login_elm.click()

        # insert 2FA
        self.observe_until_elm_id_appear("approvals_code", 5)
        mfa_elm = driver.find_element_by_id("approvals_code")
        if mfa_elm:
            mfa_elm.send_keys(self.totp.now())
        time.sleep(5)
        # Click continue (twice, once for TOTP and once for 'save browser'
        for i in range(0,5):
            try:
                self.observe_until_elm_id_appear("checkpointSubmitButton", 5)

                continue_elm = driver.find_element_by_id("checkpointSubmitButton")
                if continue_elm:
                    continue_elm.click()
                time.sleep(1)
                if driver.find_element_by_id(FacebookAuth.HEADER_PIC_ID):
                    print("Found my pic! break the loop")
                    break

            except WebDriverException as ignored:
                pass

        time.sleep(10)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(FBSanityTest)
    unittest.TextTestRunner(verbosity=2).run(suite)