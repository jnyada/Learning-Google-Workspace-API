from __future__ import print_function
from apiclient import discovery
from google.oauth2 import service_account

#creating the values to insert to theuser
DATA = {'sendAsEmail': "alias@domain.com",
        "displayName":"Alias1",
        "replyToAddress":"alias@domain.com",
        "signature":"Alias1 test",
        "isPrimary": False,
        "treatAsAlias":True,
        "verificationStatus": "accepted"
        }

SCOPES = ["https://www.googleapis.com/auth/gmail.settings.basic", "https://www.googleapis.com/auth/gmail.settings.sharing", "https://www.googleapis.com/auth/gmail.modify",  "https://www.googleapis.com/auth/gmail.send", "https://mail.google.com" ]
#declaring json file for service account
SERVICE_ACCOUNT_FILE = 'credentials.json' #path to credentials file 
#obtain credentials from the json
credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
#using the with_subject Method to pass on the credentials to the impersonated user
delegated_credentials = credentials.with_subject("user@domain.com")
#Making the call to the API
GMAIL = discovery.build('gmail', 'v1', credentials = delegated_credentials)

rsp = GMAIL.users().settings().sendAs().create(userId='user@domain.com', body=DATA).execute()
