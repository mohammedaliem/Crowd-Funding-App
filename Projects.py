import sqlite3
import re
import sys, os

class Project:
    @classmethod
    def projectScreen(cls,user_id):
        os.system('cls')

        while True:
            print("************ Project Screen ************")
            print("1-Create Project")
            print("2-View All Projects")
            print("3-Edit Project")
            print("4-Delete Project")
            print("5-Search For Project By Date")
            try:
                userInput = int(input("Please Choose From List Above: "))
            except Exception as e:
                print(e)
            else:
                if userInput == 1:
                    if cls.createProject(user_id):
                        print(f"Project is created successfully.")
                if userInput == 2:
                    cls.listProjects(user_id)
                if userInput == 3:
                    cls.editProject(user_id)
                if userInput == 4:
                    cls.deleteProject(user_id)
                if userInput == 5:
                    cls.searchForProjectByDate(user_id)

    @classmethod
    def createProject(cls , user_id):
        os.system('cls')
        try:
            conn = sqlite3.connect('crowd_funding.db')
        except Exception as ex:
            print(ex)
        else:
            while True:
                title = input("Please Enter Project Title: ")
                if bool(re.fullmatch("^[a-zA-Z]+[a-zA-Z0-9]*$", title)):
                    break
                else:
                    print("Project Title Format is incorrect")

            while True:
                details = input("Please Enter Project Details: ")
                if bool(re.fullmatch("^[a-zA-Z]+[a-zA-Z0-9]*$", details)):
                    break
                else:
                    print("Project Details Format is incorrect")

            while True:
                total_target = input("Please Enter Project Total Target: ")
                if total_target.isnumeric():
                    break
                else:
                    print("Project Total Target Format is incorrect")

            while True:
                # dd-mm-yyyy
                start_date = input("Please Enter Project Start Date dd-mm-yyyy: ")
                if bool(re.match(r"^([1-9]|1[0-9]|2[0-9]|3[0-1])(.|-)(0[1-9]|1[0-2])(.|-|)20[0-9][0-9]$" , start_date)):
                    break
                else:
                    print("Project Start Format is incorrect")
            # while True:
            #     start_date = input("Please Enter Project Start Date (DD-MM-YYYY): ")

            #             # Use regular expression to validate the date format
            #     if bool(re.match(r"^(0[1-9]|[1-2][0-9]|3[0-1])-(0[1-9]|1[0-2])-(20\d{2})$", start_date)):
            #         day, month, year = map(int, start_date.split('-'))
                            
            #                 # Additional checks for valid day and month ranges
            #         if 1 <= day <= 31 and 1 <= month <= 12:
            #                     print(f"You entered the project start date: {start_date}")
            #                     break
            #                 else:
            #                     print("Invalid day or month in the date.")
            #             else:
            #                 print("Project Start Format is incorrect. Please use DD-MM-YYYY format.")

            while True:
                end_date = input("Please Enter Project End Date as dd-mm-yyyy: ")
                if bool(re.match("^([1-9]|1[0-9]|2[0-9]|3[0-1])(.|-)(0[1-9]|1[0-2])(.|-|)20[0-9][0-9]$" , end_date)):
                    break
                else:
                    print("Project End Format is incorrect")
    
            conn.execute(f"INSERT INTO projects (user_id,title,details,total_target,start_date,end_date) \
                    VALUES ({user_id}, '{title}' , '{details}', {total_target} , '{start_date}' , '{end_date}')")
            conn.commit()
            conn.close()
            return True

    @classmethod
    def editProject(cls,user_id):
        os.system('cls')
        try:
            conn = sqlite3.connect('crowd_funding.db')
        except Exception as ex:
            print(ex)
        else:

            while True:
                project_id = input("Please Enter Project ID: ")
                project = cls.isProjectExisted(user_id,project_id)
                if project_id.isnumeric() and project:
                    break
                else:
                    print("Project ID Format is incorrect or Project is not existed")

            title = project[2]
            details = project[3]
            total_target = project[4]
            start_date = project[5]
            end_date = project[6]
            os.system('cls')
            print(f"------ Project [{title}] ------")
            while True:
                print("1-Edit Title")
                print("2-Edit Details")
                print("3-Edit Total Target")
                print("4-Edit Start Date")
                print("5-Edit End Date")
                userInput = int(input("Please Choose From List Above: "))

                if userInput == 1:
                    while True:
                        title = input("Please Enter Project Title: ")
                        if bool(re.fullmatch("^[a-zA-Z]+[a-zA-Z0-9]*$", title)):
                            break
                        else:
                            print("Project Title Format is incorrect")

                if userInput == 2:
                    while True:
                        details = input("Please Enter Project Details: ")
                        if bool(re.fullmatch("^[a-zA-Z]+[a-zA-Z0-9]*$", details)):
                            break
                        else:
                            print("Project Details Format is incorrect")

                if userInput == 3:
                    while True:
                        total_target = input("Please Enter Project Total Target: ")
                        if total_target.isnumeric():
                            break
                        else:
                            print("Project Total Target Format is incorrect")

                if userInput == 4:
                    while True:
                        start_date = input("Please Enter Project Start Date: ")
                        if bool(re.match("^([1-9]|1[0-9]|2[0-9]|3[0-1])(.|-)(0[1-9]|1[0-2])(.|-|)20[0-9][0-9]$",
                                         start_date)):
                            break
                        else:
                            print("Project Start Format is incorrect")
                

                    # while True:
                    #     start_date = input("Please Enter Project Start Date (DD-MM-YYYY): ")

                    #     # Use regular expression to validate the date format
                    #     if bool(re.match(r"^(0[1-9]|[1-2][0-9]|3[0-1])-(0[1-9]|1[0-2])-(20\d{2})$", start_date)):
                    #         day, month, year = map(int, start_date.split('-'))
                            
                    #         # Additional checks for valid day and month ranges
                    #         if 1 <= day <= 31 and 1 <= month <= 12:
                    #             print(f"You entered the project start date: {start_date}")
                    #             break
                    #         else:
                    #             print("Invalid day or month in the date.")
                    #     else:
                    #         print("Project Start Format is incorrect. Please use DD-MM-YYYY format.")


                if userInput == 5:
                    while True:
                        end_date = input("Please Enter Project End Date: ")
                        if bool(re.match("^([1-9]|1[0-9]|2[0-9]|3[0-1])(.|-)(0[1-9]|1[0-2])(.|-|)20[0-9][0-9]$",
                                         end_date)):
                            break
                        else:
                            print("Project End Format is incorrect")

                cur = conn.cursor()
                cur.execute('''UPDATE projects set title = ? , details = ? , total_target = ? , start_date = ? , end_date = ? where id = ?''' , (title,details,total_target,start_date,end_date,project_id))
                conn.commit()
                conn.close()
                break

    @classmethod
    def deleteProject(cls,user_id):
        os.system('cls')
        try:
            conn = sqlite3.connect('crowd_funding.db')
        except Exception as ex:
            print(ex)
        else:
            while True:
                project_id = input("Please Enter Project ID To Delete: ")
                project = cls.isProjectExisted(user_id,project_id)
                if project_id.isnumeric() and project:
                    break
                else:
                    print("Project ID Format is incorrect or Project is not existed")
            cur = conn.cursor()
            cur.execute(
                f'''DELETE FROM projects where id = ? and user_id = ?''',
                (project_id, user_id ))
            conn.commit()
            conn.close()
            print(f"Project ID [{project_id}] is deleted.")

    @classmethod
    def searchForProjectByDate(cls,user_id):
        os.system('cls')
        try:
            conn = sqlite3.connect('crowd_funding.db')
        except Exception as ex:
            print(ex)
        else:
            while True:
                # dd-mm-yyyy
                start_date = input("Please Enter Project Start Date: ")
                if bool(re.match("^([1-9]|1[0-9]|2[0-9]|3[0-1])(.|-)(0[1-9]|1[0-2])(.|-|)20[0-9][0-9]$" , start_date)):
                    break
                else:
                    print("Project Start Format is incorrect")

            while True:
                end_date = input("Please Enter Project End Date: ")
                if bool(re.match("^([1-9]|1[0-9]|2[0-9]|3[0-1])(.|-)(0[1-9]|1[0-2])(.|-|)20[0-9][0-9]$" , end_date)):
                    break
                else:
                    print("Project End Format is incorrect")

            cur = conn.cursor()
            cur.execute(f"SELECT * from projects where user_id = '{user_id}' and start_date = '{start_date}' and end_date = '{end_date}'")
            projects = cur.fetchall()
            for project in projects:
                id = project[0]
                title = project[2]
                details = project[3]
                total_target = project[4]
                start_date = project[5]
                end_date = project[6]
                print(f"ID : {id}")
                print(f"Title : {title}")
                print(f"Details : {details}")
                print(f"Total Target : {total_target}")
                print(f"Start Date : {start_date}")
                print(f"End Date : {end_date}")
                print("-----------------------------------------")
            conn.close()
    @classmethod
    def listProjects(cls,user_id):
        os.system('cls')
        try:
            conn = sqlite3.connect('crowd_funding.db')
        except Exception as ex:
            print(ex)
        else:
            cur = conn.cursor()
            cur.execute(f"SELECT * from projects where user_id = '{user_id}'")
            projects = cur.fetchall()
            for project in projects:
                id = project[0]
                title = project[2]
                details = project[3]
                total_target = project[4]
                start_date = project[5]
                end_date = project[6]
                print(f"ID : {id}")
                print(f"Title : {title}")
                print(f"Details : {details}")
                print(f"Total Target : {total_target}")
                print(f"Start Date : {start_date}")
                print(f"End Date : {end_date}")
                print("-----------------------------------------")
            conn.close()

    @classmethod
    def isProjectExisted(cls,user_id,project_id):
        try:
            conn = sqlite3.connect('crowd_funding.db')
        except Exception as ex:
            print(ex)
        else:
            cur = conn.cursor()
            cur.execute(f"SELECT * from projects where id = '{project_id}' and user_id = {user_id}")
            project = cur.fetchone()
            conn.close()
            if project:
                return project
            return False




