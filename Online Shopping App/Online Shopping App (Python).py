import main_menu

username = "nathan"
password = "password1234"

while True:
    print("Shopping4You")
    print("1: Log in")
    print("2: Exit")
    choice1 = int(input(""))

    if choice1 == 1:
        name = input("Username: ")
        pwd = input("Password: ")
        if name == username and pwd == password:
            print("Log in successful")
            main_menu.home_menu()
        elif name != username or pwd != password:
            print("Incorrect username or password")
        else:
            print("Invalid data: Please try again")

    if choice1 == 2:
        break
        

    
