from __future__ import print_function
import os.path
from apiclient import discovery
from googleapiclient.discovery import build
from google.oauth2 import service_account
from googleapiclient.http import MediaFileUpload

#Declaring the scopes to he used as per https://developers.google.com/drive/api/v3/reference/files/create

SCOPES = ['https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/drive.file', 'https://www.googleapis.com/auth/drive.appdata']

#declaring Domain-Wide Delegation credentials 

SERVICE_ACCOUNT_FILE = 'credentialsb.json'
#obtain credentials from the json
credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
#using the with_subject Method to pass on the credentials to the impersonated user
delegated_credentials = credentials.with_subject("user@domain.com")
#Making the call to the API
service = build('drive', 'v3', credentials=delegated_credentials)


#passing the file name and the destination format, in this case Google Spreadsheet
file_metadata = {
                'name': 'test8',
                'mimeType': 'application/vnd.google-apps.spreadsheet',
                'parents' : ['folder id of the folder inside of a shared drive']
                }

#Declaring the source file, using the file Mimetype
media = MediaFileUpload(
                     filename='test.xlsx', #name of the file, replacewith the file path and name
                      mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', # Declaring the file type using its mimetype 
                     resumable=True,
                     )

#This is the actual upload of the file 
file = service.files().create(body=file_metadata,
                              media_body=media,
                              supportsAllDrives=True, #this line allows the script to find the parent inside of a shared drive
                              fields='id').execute()
print('File ID: %s' % file.get('id'))
