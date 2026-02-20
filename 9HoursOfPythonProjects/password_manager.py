"""
desc: This app encryps and stores passwords.
"""
from cryptography.fernet import Fernet

 
"""
desc: main function for password manager app.
"""
def main():
    master_password = input("Enter the Master Password: ")
    my_key =  create_key() + master_password.encode()
    #my_key = b'81gohjHN3Fue4iUoXQn9M4fL0rZ59eLkFN3s4Vsroq4=' + master_password.encode()
    print(my_key)
    fer = Fernet(my_key)



    while True:
        print("1. Add new password")
        print("2. View passwords")
        print()
        print("9. Quit")
        print()
        
        user_input = input("Select an option: ").lower()
        if user_input.isdigit():
            match user_input:
                case "1":
                    add_password(fer)
                case "2":
                    view_passwords(fer)
                case "9":
                    print("Closing app....")
                    break
                case _:
                    print("Invalid Input. Select a valid option.")
                    print()
                    continue

        else:
            print("Enter a number to select an option")
            print()
            continue


def add_password(fer):
    account_name = input("Account name: ")
    account_password = input("Account Password: ")

    with open("passwords.txt", "a") as file:
        file.write(f"{account_name}|{fer.encrypt(account_password.encode()).decode()}\n")



def view_passwords(fer):
    with open("passwords.txt", "r") as file:
        for i, each_line in enumerate(file):
            name, passw = each_line.rstrip().split("|") #rstrip() prevents the \n feature from being read
            print(f"{i + 1}) Account name: {name} | Account Password: {fer.decrypt(passw.encode()).decode()}")

    input("Press ENTER to continue...")
    print()


def create_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

    return key

if __name__ == "__main__":
    main()