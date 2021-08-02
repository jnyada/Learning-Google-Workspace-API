from __future__ import print_function
from apiclient import discovery
from httplib2 import Http
from google.oauth2 import service_account

#creating the values to insert to theuser
DATA = {'signature': "WASAMARA LA YUCA \n\nhecho con gmail api"}

SCOPES = ["https://www.googleapis.com/auth/gmail.settings.basic", "https://www.googleapis.com/auth/gmail.modify", "https://www.googleapis.com/auth/gmail.send", "https://mail.google.com" ]
#declaring json file for service account
SERVICE_ACCOUNT_FILE = 'credentials3.json'
#obtain credentials from the json
credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
#using the with_subject Method to pass on the credentials to the impersonated user
delegated_credentials = credentials.with_subject("rene@support-domain26.info")
#Making the call to the API
GMAIL = discovery.build('gmail', 'v1', credentials = delegated_credentials)

addresses = GMAIL.users().settings().sendAs().list(userId="rene@support-domain26.info", fields='sendAs(isPrimary, sendAsEmail)').execute().get('sendAs')

for address in addresses:
    if address.get('isPrimary'):
        break

rsp = GMAIL.users().settings().sendAs().patch(userId='rene@support-domain26.info', sendAsEmail = address['send'], body=DATA).execute()
