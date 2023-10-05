import sqlite3
import re
import getpass
import sys, os

class Authentication:
    @classmethod
    def register(cls):
        os.system('cls')

        try:
            conn = sqlite3.connect('crowd_funding.db')
        except Exception as ex:
            print(ex)
        else:
            while True:
                firstName = input("Please Enter Your First Name: ")
                if bool(re.fullmatch("^[a-zA-Z]+[a-zA-Z0-9]*$", firstName)):
                    break
                else:
                    print("First Name Format is incorrect")
            while True:
                lastName = input("Please Enter Your Last Name: ")
                if bool(re.match("^[a-zA-Z]+[a-zA-Z0-9]*$", lastName)):
                    break
                else:
                    print("Last Name Format is incorrect")
            while True:
                email = input("Please Enter Your Email: ")
                if bool(re.fullmatch("^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$", email)):
                    if not cls.isUserExisted(email):
                        break
                    else:
                        print("Email is already exists")
                else:
                    print("Email Format is incorrect")
            while True:
                password = getpass.getpass('Please Enter your password: ')
                # Minimum six characters, at least one letter and one number:
                if bool(re.fullmatch("^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{6,}$", password)):
                    break
                else:
                    print("Password must be Minimum six characters, at least one letter and one number")
            while True:
                password_confirmation = getpass.getpass("Please Enter Your Password Confirmation: ")
                if password == password_confirmation:
                    break
                else:
                    print("Password Confirmation is incorrect")
            while True:
                phone_number = input("Please Enter Your Phone Number: ")
                if bool(re.match("^01[0125][0-9]{8}$", phone_number)):
                    break
                else:
                    print("Phone Number Format is incorrect")

            conn.execute(f"INSERT INTO users (first_name,last_name,email,password,phone) \
                      VALUES ('{firstName}', '{lastName}' , '{email}', '{password}' , '{phone_number}'  )")
            conn.commit()
            conn.close()
            print(f"{firstName} {lastName} is created successfully.")
            return True

    @classmethod
    def login(cls):
        os.system('cls')

        while True:
            userInputEmail = input("Please Enter Your Email: ")
            if bool(re.match("^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$", userInputEmail)):
                break
            else:
                print("Email Format is incorrect")
        while True:
            userInputPassword = getpass.getpass('Please Enter your password: ')
            # Minimum six characters, at least one letter and one number:
            if bool(re.fullmatch("^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{6,}$", userInputPassword)):
                break
            else:
                print("Password must be Minimum six characters, at least one letter and one number")
        user = cls.isUserExisted(userInputEmail)
        if user:
            return user
        return False


    @classmethod
    def isUserExisted(cls, email):
        try:
            conn = sqlite3.connect('crowd_funding.db')
        except Exception as ex:
            print(ex)
        else:
            cur = conn.cursor()
            cur.execute(f"SELECT * from users where email = '{email}'")
            user = cur.fetchone()
            conn.close()
            if user:
                return user
            return False



