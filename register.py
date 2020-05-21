import json
import os
from os.path import join, dirname

from cryptography.fernet import Fernet
from dotenv import load_dotenv
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

KEY = os.environ.get("KEY")
cipher_suite = Fernet(KEY)


def register():
    print("\nWelcome to Darkcodelab\n")
    username = input("Enter a unique username: ")
    password = input("Enter a strong password: ")
    password = str.encode(password)
    password = cipher_suite.encrypt(password)
    password = password.decode()

    stringFile = {username: password}
    jsonFile = json.dumps(stringFile)

    with open('passfile.json', "r+") as pass_file:
        data = json.load(pass_file)
        jsonFile = json.loads(jsonFile)
        data.update(jsonFile)
        pass_file.seek(0)
        json.dump(data, pass_file)

    print("User added")


register()
