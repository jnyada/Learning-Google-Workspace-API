from __future__ import print_function
from apiclient import discovery
from google.oauth2 import service_account

#creating the values to insert to theuser
DATA = {'signature': '"Watching. Potential. Learn. Grow. Provoke. Consume. Reward. Patience." \n - Ukotoa"'}

SCOPES = ["https://www.googleapis.com/auth/gmail.settings.basic", "https://www.googleapis.com/auth/gmail.modify", "https://www.googleapis.com/auth/gmail.send", "https://mail.google.com" ]
#declaring json file for service account
SERVICE_ACCOUNT_FILE = 'credentials.json' #this file is created from a project on google cloud platform.
#obtain credentials from the json
credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
#using the with_subject Method to pass on the credentials to the impersonated user
delegated_credentials = credentials.with_subject("user@domain.com")
#Making the call to the API
GMAIL = discovery.build('gmail', 'v1', credentials = delegated_credentials)

rsp = GMAIL.users().settings().sendAs().patch(userId='user@domain.com', sendAsEmail = 'user@domain.com', body=DATA).execute()
