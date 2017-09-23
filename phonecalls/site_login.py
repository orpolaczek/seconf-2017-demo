import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import unittest
from utils.gcloud_transcript import GCloudTranscript

class SiteSanityTest(unittest.TestCase):

    def get_incognito_caps(self):
        options = Options()
        options.add_argument("-incognito")
        options.add_argument("--disable-popup-blocking")
        return options

    def setUp(self):
        self.driver = webdriver.Chrome('/usr/local/bin/chromedriver',
                                       chrome_options=self.get_incognito_caps())
        self.gcloudTranscriber = GCloudTranscript()

    def tearDown(self):
        self.driver.quit()

    def test_login_with_phone_verification(self):
        driver = self.driver

        recording_file_path = os.path.join(
            os.path.dirname(__file__),
            'recordings',
            'latest-record.wav')

        transcripts = self.gcloudTranscriber.transcribe_file(recording_file_path)
        print(transcripts[0])

        #driver.get("http://www.facebook.com")
        #time.sleep(10)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SiteSanityTest)
    unittest.TextTestRunner(verbosity=2).run(suite)