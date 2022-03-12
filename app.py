from pathlib import Path
import sys # for sys.exit()

PASSWORDS_FILE = Path('passwords.txt')
MASTER_PASSWORD_FILE = Path('master_password.txt')

password_verified = False

def set_up_master_password():
    while True:
        master_password = input("Please set up your master password: ")
        master_password_repeat = input("Repeat your master password: ")

        if master_password != master_password_repeat:
            print("Passwords are not the same.")
        else:
            with open(MASTER_PASSWORD_FILE, 'w') as file:
                file.write(master_password)
            break

def verify_master_password():
    while True:
        master_password = input("Please enter your master password: ")
        with open(MASTER_PASSWORD_FILE, 'r') as file:
            if file.readline() == master_password:
                global password_verified
                password_verified = True
                return True
            print("Wrong password")

def choose_option():
    while True:
        print("ADD - add new password")
        print("VIEW - view existing passwords")
        print("CHANGE - change your master password")
        print("Q - quit")
        option = input("Choose what you want to do: ").lower()
        if option == 'add' or option == 'view' or option == 'change' or option == 'q':
            return option
        print("Not a valid choose")

def add_password():
    username = input("Enter username: ")
    password = input("Enter password: ")
    app = input("Enter app name or website: ")
    with open(PASSWORDS_FILE, 'a') as file:
        file.write(f"{username}/{password}/{app}\n")

def view_passwords():
    if PASSWORDS_FILE.exists():
        with open(PASSWORDS_FILE, 'r') as file:
            for line in file:
                username, password, app = line.rstrip().split('/')
                print(f"Username: {username}, password: {password}, app/website: {app}")
    else:
        print("You must add some passwords first.")

# PROGRAM STARTS HERE
if not MASTER_PASSWORD_FILE.exists():
    set_up_master_password()
else:
    verify_master_password()

if password_verified:
    match choose_option():
        case 'add':
            add_password()
        case 'view':
            view_passwords()
        case 'change':
            set_up_master_password()
        case 'q':
            sys.exit()
        case _:
            print("Error")