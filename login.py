import json
import os
from os.path import join, dirname

from cryptography.fernet import Fernet
from dotenv import load_dotenv
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

KEY = os.environ.get("KEY")
# KEY is jibGzGCKrT0kmc_sQepUImgG8qkzDyVfOlgWGcGZxBw=
cipher_suite = Fernet(KEY)
# print(KEY)


exitState = True


# def loggedin(username):
# executes after logging in successfully


def login():

    print("\nWelcome to Darkcodelab\n")
    username = input('Enter Your Username: ')
    password = input("Enter Your Password: ")

    with open('passfile.json') as pass_file:
        data = json.load(pass_file)

        if(username in data):
            pass_as_bytes = str.encode(data[username])
            decrypted_pass = cipher_suite.decrypt(pass_as_bytes)
            if(password == decrypted_pass.decode()):
                print(f"\nwelcome {username}")
                # while exitState:
                #     loggedin(username)

            else:
                print("password is wrong")
        else:
            print(
                "Username not found. If you are not registered. Run register.py to register")


login()
