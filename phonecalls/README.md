
https://developers.google.com/accounts/docs/application-default-credentials

https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/speech/cloud-client/quickstart.py

export GOOGLE_APPLICATION_CREDENTIALS="SeConf-2017-Demo-ca6452ecebd2.json"


https://dashboard.nexmo.com/getting-started-guide

nexmo app:create "SeConf 2017 demo app" https://example.com \
https://example.com --type=voice --keyfile=private.key

app_id = 4030504b-1ba2-4ef0-815d-03c51afefc85
APP_JWT="$(nexmo jwt:generate ./private.key \
application_id=4030504b-1ba2-4ef0-815d-03c51afefc85)"





curl -X POST https://api.nexmo.com/v1/calls\
  -H "Authorization: Bearer "$APP_JWT\
  -H "Content-Type: application/json"\
  -d '{"to":[{"type": "phone","number": 972523022969}],
      "from": {"type": "phone","number": 12345678901},
      "answer_url":["https://integrated.co.il/seconf/nexmo_voice_response.php?text=Hello,%20This%20is%20a%20demo%20from%20SeConf%202017.%20Your%20code%20is%202323"]}'