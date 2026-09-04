import json
import os

archive = "credentials.json"


def read_credentials():
    if os.path.exists(archive):
        try:
            with open(archive, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {}
    return {}

def add_credentials(credentials):
    with open(archive, "w") as f:
        json.dump(credentials, f)

credentials = read_credentials()

while True:
    answer = input("Do you have an account? (yes/no): ")
    if answer == "yes":
        user = input("Introduce user: ")
        password = input("Introduce password: ")
        if(credentials[user] == password):
            print("Succesfully sign-in")
            break
        else:
            print("Your credentials don't match, try creating a new account")
    print("let's create you an account")
    user = input("Introduce user: ")
    password = input("Introduce password: ")
    credentials[user] = password
    add_credentials(credentials)

print(f"Hi, {user}!")