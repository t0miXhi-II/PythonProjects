import sys

try: 
    email = sys.argv[1]

except IndexError:
    print("No email was provided via the command line")
    email = input("Please enter a valid email address: ")
    #sys.exit(1)

try:
    email_username = email[: email.index('@')]
    email_domain = email[email.index('@') + 1 : ]

except ValueError:
    print("Invalid Email address provided")
    print("Try again")
    sys.exit(1)

print(f"Username: {email_username}")
print(f"Domian: {email_domain}")