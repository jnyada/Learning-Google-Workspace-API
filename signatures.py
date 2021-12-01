from __future__ import print_function
from apiclient import discovery
from google.auth import credentials
from google.oauth2 import service_account
from oauth2client.client import SERVICE_ACCOUNT

def targets():
    targets = []
    SCOPES = ['https://www.googleapis.com/auth/admin.directory.user', 'https://www.googleapis.com/auth/admin.directory.user.readonly', 'https://www.googleapis.com/auth/cloud-platform']
    SERVICE_ACCOUNT_FILE= 'credentials.json'
    credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    creds = credentials.with_subject("admin@domain.com")
    service = discovery.build('admin', 'directory_v1', credentials=creds)

    results = service.users().list(customer='customer_id', maxResults=10, orderBy= 'email',query='String').execute()
    #the query is optional
    users = results.get('users', [])
    for user in users:
        targets.append(u'{0}'.format(user['primaryEmail']))
    
    return targets

def signature(target):
    #creating the values to insert to theuser
    DATA = {'signature': '"updating signatures for multiple userswith a couple of functions I made." \n - Yada"'}

    SCOPES = ["https://www.googleapis.com/auth/gmail.settings.basic", "https://www.googleapis.com/auth/gmail.modify", "https://www.googleapis.com/auth/gmail.send", "https://mail.google.com" ]
    #declaring json file for service account
    SERVICE_ACCOUNT_FILE = 'credentialsb.json' #this file is created from a project on google cloud platform.
    #obtain credentials from the json
    credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    #using the with_subject Method to pass on the credentials to the impersonated user
    delegated_credentials = credentials.with_subject(target)
    #Making the call to the API
    GMAIL = discovery.build('gmail', 'v1', credentials = delegated_credentials)

    rsp = GMAIL.users().settings().sendAs().patch(userId=target, sendAsEmail = target, body=DATA).execute()

users = targets()

for user in users:
    signature(user)
