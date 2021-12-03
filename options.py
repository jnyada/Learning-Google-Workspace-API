from __future__ import print_function
from apiclient import discovery
from google.oauth2 import service_account

def main():
    print("Available options:")
    print("1 -> List All Users (Name and Primary Email)")
    print("2 -> List all users' Email Aliases")
    print("3 -> List Available attributes ")
    print("4 -> Exit ")
    x = int(input("Choose An option: "))
    if x == 1: 
        users = get_users()
        list_users(users)

    elif x == 2:
        users = get_users()
        aliases(users)
    elif x == 3:
        users = get_users()
        get_keys(users)
    elif x == 4:
        print("Bye!")
    else:
        print("Wrong Input try again")
        main()

        #has_2sv(users)


def get_users():
    
    SCOPES = ['https://www.googleapis.com/auth/admin.directory.user', 'https://www.googleapis.com/auth/admin.directory.user.readonly', 'https://www.googleapis.com/auth/cloud-platform']
    SERVICE_ACCOUNT_FILE= 'credentials.json'
    credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    creds = credentials.with_subject("admin@domain.com")
    service = discovery.build('admin', 'directory_v1', credentials=creds)

    response = service.users().list(domain='domain.com', maxResults=50, orderBy= 'email').execute()
    users = response.get('users')
    
    return users

def get_keys(users):
    for user in users:
        for key in user:
            print("->", key)
        break
    main()      

def list_users(users):
    for user in users:
        print(u'{0} ({1})'.format(user['primaryEmail'], user['name']['fullName']))
    main()

def aliases(users):    
    for user in users:
        print(user['primaryEmail'])
        keyname = 'aliases'
        if keyname in user:
            print(user['aliases'])
        else:
            print("User has no aliases")
            continue
    main()
    
def has_2sv(users):
    for user in users:
        print(user['primaryEmail'])
        print(user['isEnrolledIn2Sv'])
    main()

if __name__ == '__main__':
    main()
