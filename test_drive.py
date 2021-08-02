from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from httplib2 import Http
from google.oauth2 import credentials, service_account

SCOPES = ["https://www.googleapis.com/auth/drive"]

SERVICE_ACCOUNT_FILE = 'credentials.json'
credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes= SCOPES)
delegated_creds = credentials.with_subject("user@domain")

service = build('drive', 'v3', credentials = delegated_creds)

results = service.files().list(orderBy = 'name', pageSize = 10, corpora= 'user').execute()
items = results.get('files', [])

if not items:
    print("no files found")
else:
    print("files:")
    for item in items:
        print(u'{0} ({1})'.format(item['name'], item['id']))

#print(results)
