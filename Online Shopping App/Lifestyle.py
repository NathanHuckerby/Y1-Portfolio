import main_menu
import time

def noBal():
    print("Unable to purchase item: Insufficient funds")
    main_menu.home.menu()

def health():
        print("|          Health             |")
        print("-------------------------------")
        print("| Toothpaste (1x4)      : £12 |")
        print("| Toothbrush            : £17 |")
        print("| Shampoo & Conditioner : £20 |")
        print("| Vitamins              : £7  |")
        print("-------------------------------")
        buy = input("Would you like to purchase an item: ")
        if buy == "yes".capitalize():
            purch = input("Please select one of the items: ")
            if purch == "toothpaste".capitalize():
                if main_menu.balance < 12:
                    noBal()
                else:
                    main_menu.balance - 12
                    print("You have purchased Toothpaste (1x4)")
                    time.sleep(1)
                    print("Your total balance is now:", main_menu.balance)
                    lifestyle()
            if purch == "toothbrush".capitalize():
                if main_menu.balance < 17:
                    noBal()
                else:
                    main_menu.balance - 17
                    print("You have purchased Toothbrush")
                    time.sleep(1)
                    print("Your total balance is now:", main_menu.balance)
                    lifestyle()
            if purch == "shampoo".capitalize() or "shampoo and conditioner".capitalize() or "shampoo & conditioner".capitalize():
                if main_menu.balance < 20:
                    noBal()
                else:
                    main_menu.balance - 20
                    print("You have purchased Shampoo & Conditioner")
                    time.sleep(1)
                    print("Your total balance is now:", main_menu.balance)
                    lifestyle()
            if purch == "vitamins".capitalize():
                if main_menu.balance < 7:
                    noBal()
                else:
                    main_menu.balance - 7
                    print("You have purchased Vitamins")
                    time.sleep(1)
                    print("Your total balance is now:", main_menu.balance)
                    lifestyle()
        if buy == "no".capitalize():
            print("\n")
            print("-------------------------------")
            print("| Redirecting to home page... |")
            print("-------------------------------")
            time.sleep(1)
            main_menu.home_menu()

def home():
        print("\n")
        print("|         Home           |")
        print("--------------------------")
        print("| Sofa            : £150 |")
        print("| Washing machine : £250 |")
        print("| Dining table    : £150 |")
        print("| Bed mattress    : £100 |")
        print("--------------------------")
        buy = input("Would you like to purchase an item: ")
        if buy == "yes".capitalize():
            purch = input("Please select one of the items: ")
            if purch == "sofa".capitalize():
                if main_menu.balance < 150:
                    noBal()
                else:
                    main_menu.balance - 150
                    print("You have purchased Sofa")
                    time.sleep(1)
                    print("Your total balance is now:", main_menu.balance)
                    home()
            if purch == "washing machine".capitalize():
                if main_menu.balance < 250:
                    noBal()
                else:
                    main_menu.balance - 250
                    print("You have purchased Washing machine")
                    time.sleep(1)
                    print("Your total balance is now:", main_menu.balance)
                    home()
            if purch == "dining table".capitalize() or "table".capitalize():
                if main_menu.balance < 150:
                    noBal()
                else:
                    main_menu.balance - 150
                    print("You have purchased Dining table")
                    time.sleep(1)
                    print("Your total balance is now:", main_menu.balance)
                    home()
            if purch == "bed mattress".capitalize() or "mattress".capitalize():
                if main_menu.balance < 100:
                    noBal()
                else:
                    main_menu.balance - 100
                    print("You have purchased Bed mattress")
                    time.sleep(1)
                    print("Your total balance is now:", main_menu.balance)
                    home()
        if buy == "no".capitalize():
            print("\n")
            print("-------------------------------")
            print("| Redirecting to home page... |")
            print("-------------------------------")
            time.sleep(1)
            main_menu.home.menu()





def lifestyle():
    print("\n")
    print("|        Lifestyle        |")
    print("---------------------------")
    print("| Health | Home | Beauty | ")
    print("---------------------------")
    print("\n")
    pick = input("")

    if pick == "health".capitalize():
        health()
    

    if pick == "home".capitalize():
        home()
                    