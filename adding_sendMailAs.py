from __future__ import print_function
from apiclient import discovery
from google.oauth2 import service_account

#creating the values to insert to theuser
DATA = {'sendAsEmail': "testingapi@support-domain26.info",
        "displayName":"Alias1",
        "replyToAddress":"testingapi@support-domain26.info",
        "signature":"Alias1 test",
        "isPrimary": False,
        "treatAsAlias":True,
        "verificationStatus": "accepted"
        }

SCOPES = ["https://www.googleapis.com/auth/gmail.settings.basic", "https://www.googleapis.com/auth/gmail.settings.sharing", "https://www.googleapis.com/auth/gmail.modify",  "https://www.googleapis.com/auth/gmail.send", "https://mail.google.com" ]
#declaring json file for service account
SERVICE_ACCOUNT_FILE = 'adding-aliases.json'
#obtain credentials from the json
credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
#using the with_subject Method to pass on the credentials to the impersonated user
delegated_credentials = credentials.with_subject("yadatest@support-domain26.info")
#Making the call to the API
GMAIL = discovery.build('gmail', 'v1', credentials = delegated_credentials)

rsp = GMAIL.users().settings().sendAs().create(userId='yadatest@support-domain26.info', body=DATA).execute()