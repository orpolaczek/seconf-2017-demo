import nexmo
import requests

class NexmoClient:
    def __init__(self):
        with open("../private.key", 'r') as keyfile:
            self.client = nexmo.Client(application_id="4030504b-1ba2-4ef0-815d-03c51afefc85", private_key=keyfile.read())

    def call_with_code(self, to, code):
        requests.get("http://integrated.co.il/seconf/nexmo_voice_response.php?text=Hello, This is a demo from Selenium Conference 2017. Your code is {}".format(code))

        response = self.client.create_call({
            'to': [{'type': 'phone', 'number': to}],
            'from': {'type': 'phone', 'number': '97239000000'},
            'answer_url': ['http://www.integrated.co.il/seconf/answer.json']
        })

        print(response)

if __name__ == '__main__':
    client = NexmoClient()
    client.call_with_code('972722701610', "1223")