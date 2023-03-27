import time
import csv



student_details = []

def send(): 
        with open('student.csv', 'a', encoding='UTF8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(student_details)
                f.close()
def read():
        with open('student.csv', 'r') as file:
                lines = []
                for line in file:
                        lines.append(line.rstrip())
                return lines
    
        
username = "MrLeeman"
password="mrLeeman16"


def login():
    user = input("Please enter your username.")
    passw = input("Please enter your password.")
    if user == username and passw == password:
            print("You have successfully logged in")
    if user != username or passw != password:
            print("Incorrect username or password")
            login()
            
        
login()
time.sleep(1.5)
def menu():
    print("Hello! Welcome to Tree Road School administration system.")
    time.sleep(0.5)
    print("Please choose from the following options:")
    time.sleep(0.5)
    print("1. Enter student details")
    time.sleep(0.5)
    print("2. Retrieve & display student details")
    time.sleep(0.5)
    print("3. Create report")
    time.sleep(0.5)
    print("4. Log out")
    time.sleep(0.5)
    
menu()

while True:
        user = int(input(""))
        if user == 1:
                ID = int(input("Please enter the student's ID number"))
                student_details.append(ID)
                surname = input("Please enter the student's surname")
                student_details.append(surname)
                forname = input("Please enter the student's forname")
                student_details.append(forname)
                date_of_birth = input("Please enter the student's date of birth")
                student_details.append(date_of_birth)
                home_address = input("Please enter the student's home address")
                student_details.append(home_address)
                home_phone_number = int(input("Please enter the student's home phone number"))
                student_details.append(home_phone_number)
                gender = input("Please enter the student's gender")
                student_details.append(gender)
                tutor_group = input("Please enter the student's tutor group")
                student_details.append(tutor_group)
                school_email_address = input("Please enter the student's school email address")
                student_details.append(school_email_address)
                age = int(input("Please enter student's age"))
                student_details.append(school_email_address)
                print(student_details)
                send()


        
        if user == 2:
                studentID = input("Enter student's ID number")
                csv_file = csv.reader(open("student.csv", "r"), delimiter=",")
                for row in csv_file:
                        if studentID == row[0]:
                                print(row)

        if user == 3:
               male = 0
               female = 0
               csv_file = csv.reader(open("student.csv", "r"), delimiter=",")
               for row in csv_file:
                        if "Male" == row[6]:
                                male = male + 1
                        elif "Female" == row[6]:
                                female = female + 1
               print("There are ", male, "males in the tutor group")
               print("There are ", female, "females in the tutor group")
        menu()

        if user == 4:
                print("You are now logged out")
                                       

    
