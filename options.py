#
# THIS IS WIP
#
from __future__ import print_function
from apiclient import discovery
from google.oauth2 import service_account

def main():
    print("\nAvailable options:")
    print("1 -> List All Users (Name and Primary Email)")
    print("2 -> List all users' Email Aliases")
    print("3 -> List Available attributes ")
    print("4 -> List Super Admins ")
    print("5 -> List users with 2SV enabled ")
    print("6 -> List users last login time ")
    print("7 -> Remove change Password at next login flag")
    print("0 -> Exit ")
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
        users = get_users()
        get_SAdmins(users)
    elif x == 5:
        users = get_users()
        has_2sv(users)
    elif x == 6:
        users = get_users()
        get_last_login(users)
    elif x == 7:
        users = get_users()
        chg_pwd_nlogin(users)
        '''elif y == '1':
            z = input("Enter Email address: ")
        else:
            print("Wrong input")'''


        
    elif x == 0:
        print("Bye!")
    else:
        print("Wrong Input try again")
        main()


def get_users():
    
    SCOPES = ['https://www.googleapis.com/auth/admin.directory.user', 'https://www.googleapis.com/auth/admin.directory.user.readonly', \
	      'https://www.googleapis.com/auth/cloud-platform']
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
        if user['isEnrolledIn2Sv'] == True:
            print(user['primaryEmail'])
        else:
            continue
    main()

def get_SAdmins(users):
    for user in users:
        if user['isAdmin'] == True:
            print(user['primaryEmail'])
    main()
def get_last_login(users):
    for user in users:
        print(user['lastLoginTime'])

def chg_pwd_nlogin(users):
    #This is a WIP currently it changes  all users to False. Still working on passing a single user
    # I need to learn about optional arguments 
    SCOPES = ['https://www.googleapis.com/auth/admin.directory.user']
    SERVICE_ACCOUNT_FILE= 'credentialsc.json'
    credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    creds = credentials.with_subject("admin@domain.com")
    service = discovery.build('admin', 'directory_v1', credentials=creds)

    for user in users:
        if user['changePasswordAtNextLogin'] == True:
            print(user['primaryEmail'], user['changePasswordAtNextLogin'])
            rsp = service.users().patch(userKey = user['id'], body= { "changePasswordAtNextLogin" : False}).execute()

            print(rsp['primaryEmail'], "is now", rsp['changePasswordAtNextLogin'])
        else:
            continue
    print("Done!")
    main()    

if __name__ == '__main__':
    main()
