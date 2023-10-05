# from Authentication import Authentication
# from Projects import Project
# import sys, os
# def welcomeScreen():
#     while True:
#         print("Welcome To CroedFunding By Mohammed Ali AbdelAleem")
#         print("1-Sign Up")
#         print("2-Sign In")
#         try:
#             userInput = int(input("Please Choose From List Above: "))
#         except Exception as e:
#             print(e)
#         else:
#             if userInput == 1:
#                 if Authentication.register():
#                     print("You can login now")
#             elif userInput == 2:
#                 user = Authentication.login()
#                 if user:
#                     user_id = user[0]
#                     print("Logged In")
#                     Project.projectScreen(user_id)
#                 else:
#                     print("user is not exists.")


# welcomeScreen()
import os
from Authentication import Authentication
from Projects import Project
import sys

def clear_screen():
    if sys.platform == 'win32':
        os.system('cls')  # For Windows
    else:
        os.system('clear')  # For Linux and macOS

def welcomeScreen():
    while True:
        clear_screen()
        print("Welcome To CrowdFunding By Mohammed Ali AbdelAleem")
        print("1-Sign Up")
        print("2-Sign In")
        try:
            userInput = int(input("Please Choose From List Above: "))
        except ValueError as e:
            print(e)
        else:
            if userInput == 1:
                if Authentication.register():
                    print("You can login now")
            elif userInput == 2:
                user = Authentication.login()
                if user:
                    user_id = user[0]
                    print("Logged In")
                    Project.projectScreen(user_id)
                else:
                    print("User does not exist.")

if __name__ == "__main__":
    welcomeScreen()
