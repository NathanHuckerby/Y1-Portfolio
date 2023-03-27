import main_menu
import time
def noBal():
    print("Unable to purchase item: Insufficient funds")
    main_menu.home.menu()


def gaming():
    print("\n")
    print("|          Gaming          |")
    print("----------------------------")
    print("| Xbox One            : £200")
    print("| Meta Quest Pro      : £900")
    print("| PlayStation 5       : £600")
    print("| Nintendo Switch     : £100")
    print("| Acer Predator Orion : £1000")
    print("----------------------------")
    time.sleep(1)
    buy = input("Would you like to purchase an item: ")
    if buy == "yes".capitalize():
        purch = input("Please select one of the items")
        if purch == "xbox one".capitalize():
            if main_menu.balance < 200:
                noBal()
            else:
                main_menu.balance - 200
                print("You have purchased Xbox One")
                time.sleep(1)
                print("Your total balance is now:", main_menu.balance)
                gaming()
        if purch == "meta".capitalize() or "meta quest pro".capitalise():
            if main_menu.balance < 900:
                noBal()
            else:
                main_menu.balance - 900
                print("You have purchased Meta Quest Pro")
                time.sleep(1)
                print("Your total balance is now:", main_menu.balance)
                gaming()
        if purch == "playstation 5".capitalize() or "playstation".capitalize():
            if main_menu.balance < 600:
                noBal()
            else:
                main_menu.balance - 600
                print("You have purchased PlayStation 5")
                time.sleep(1)
                print("Your total balance is now:", main_menu.balance)
                gaming()
        if purch == "nintendo switch".capitalize():
            if main_menu.balance < 100:
                noBal()
            else:
                main_menu.balance - 100
                print("You have purchased Nintendo Switch")
                time.sleep(1)
                print("Your total balance is now:", main_menu.balance)
                gaming()
        if purch == "acer".capitalize() or "acer predator orion".capitalize():
            if main_menu.balance < 1000:
                noBal()
            else:
                main_menu.balance - 1000
                print("You have purchased Acer Predator Orion")
                time.sleep(1)
                print("Your total balance is now:", main_menu.balance)
                gaming()
    if buy == "no".capitalize():
        print("\n")
        print("-------------------------------")
        print("| Redirecting to home page... |")
        print("-------------------------------")
        time.sleep(1)
        main_menu.home_menu()



    
def phones():
    print("\n")
    print("|          Phones            |")
    print("------------------------------")
    print("| iPhone 14 Pro Max  : £700  |")
    print("| Google Pixel 7     : £400  |")
    print("| Samsung Galaxy S22 : £500  |")
    print("| iPhone 13          : £300 |")
    print("------------------------------")
    buy = input("Would you like to purchase an item: ")
    if buy == "yes".capitalize():
        purch = input("Please select one of the items: ")
        if purch == "iphone 14".capitalize():
            if main_menu.balance < 700:
                noBal()
            else:
                main_menu.balance - 700
                print("You have purchased iPhone 14 Pro Max")
                time.sleep(1)
                print("Your total balance is now:", main_menu.balance)
                phones()
        if purch == "pixel 7".capitalize() or "google pixel 7".capitalize():
            if main_menu.balance < 400:
                noBal()
            else:
                main_menu.balance - 400
                print("You have purchased Google Pixel 7")
                time.sleep(1)
                print("Your total balance is now:", main_menu.balance)
                phones()
        if purch == "galaxy s22".capitalize() or "samsung galaxy s22".capitalize():
            if main_menu.balance < 500:
                noBal()
            else:
                main_menu.balance - 500
                print("You have purchased Samsung Galaxy S22")
                time.sleep(1)
                print("Your total balance is now:", main_menu.balance)
                phones()
        if purch == "iphone 13".capitalize():
            if main_menu.balance < 300:
                noBal()
            else:
                main_menu.balance - 300
                print("You have purchased iPhone 13")
                time.sleep(1)
                print("Your total balance is now:", main_menu.balance)
                phones()
    if buy == "no".capitalize():
        print("\n")
        print("-------------------------------")
        print("| Redirecting to home page... |")
        print("-------------------------------")
        time.sleep(1)
        main_menu.home_menu()




            