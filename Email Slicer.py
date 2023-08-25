#This app slices an inputed email address to extract the username and the domain

def getEmail():
    email = input("Please enter your email address: ")
    return email

def getUsername(email):
    username = email[:email.index('@')]
    print(f"Your Username is: {username}")
    return username

def getEmailDomain(email):
    domian = email[email.index('@') + 1 :]
    print(f"Your Domian is: {domian}")
    return domian


email = getEmail()
getUsername(email)
getEmailDomain(email)