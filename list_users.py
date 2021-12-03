from __future__ import print_function
from apiclient import discovery
from google.oauth2 import service_account
#This file was created to explain my current understanding of both Python and Google's API request and Response

def main():
    SCOPES = ['https://www.googleapis.com/auth/admin.directory.user', 'https://www.googleapis.com/auth/admin.directory.user.readonly', 'https://www.googleapis.com/auth/cloud-platform']
    #SCOPES that are required to be used for listing users as detailed at https://developers.google.com/admin-sdk/directory/reference/rest/v1/users/list#authorization-scopes
    SERVICE_ACCOUNT_FILE= 'credentials.json' #Path to the credentials file created from a Service account at console.cloud.google.com
    credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    creds = credentials.with_subject("admin@domain.com")
    service = discovery.build('admin', 'directory_v1', credentials=creds)

    response = service.users().list(domain='domain.com', maxResults=10, orderBy= 'email',query='yada').execute()
    #the response is a JSON Object, due to its syntax python will recognize it as a Dictonary, the next line confirms this
    print( "'response' is a " , type(response) , " type, with ", len(response),  " items:")
    for key in response:
        print("->", key) #As per https://developers.google.com/admin-sdk/directory/reference/rest/v1/users/list#response-body there should only be 3 results, only 3 keys
    
    users = response.get('users') #here we are creating a new list, one of the values from the dict 'response' is 'users' which is a list made up of other dictonaries
    print( "'users' is a " , type(users) , " type, with ", len(users),  " items")
    for user in users:
        print("'user' is a " , type(user) , " type, with ", len(user),  " items:") #user is a new dictonary with multiple keys, depending on the user
        for key in user:
            print("->", key)
        print((user['primaryEmail']))
 
