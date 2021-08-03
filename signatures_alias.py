from __future__ import print_function
from apiclient import discovery
from httplib2 import Http
from google.oauth2 import service_account

#creating the values to insert to theuser
DATA = {'signature': "Test Signature"}

SCOPES=["https://www.googleapis.com/auth/gmail.settings.basic","https://www.googleapis.com/auth/gmail.modify","https://www.googleapis.com/auth/gmail.send","https://mail.google.com"]
#declaring json file for service account
SERVICE_ACCOUNT_FILE = 'credentials.json'
""" obtain credentials from the json file and pass them on to the delegated account 
using impersonation as explained on https://developers.google.com/identity/protocols/oauth2/service-account#authorizingrequests """
credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
delegated_credentials = credentials.with_subject("user@domain")
#Making the call to the API
GMAIL = discovery.build('gmail', 'v1', credentials = delegated_credentials)

addresses = GMAIL.users().settings().sendAs().list(userId="user@domain", fields='sendAs(isPrimary, sendAsEmail)').execute().get('sendAs')

for address in addresses:
    if address.get('isPrimary'):
        break

rsp = GMAIL.users().settings().sendAs().patch(userId='user@domain', sendAsEmail = address['send'], body=DATA).execute()
