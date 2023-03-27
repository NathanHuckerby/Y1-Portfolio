import main_menu
import time
def noBal():
    print("Unable to purchase item: Insufficient funds")
    main_menu.home.menu()

def Tshirt():
    print("\n")
    print("|          T-shirts             |")
    print("---------------------------------")
    print("| Underarmour T-shirt     : £9  |")
    print("| T-shirt multipack (1x5) : £18 |")
    print("| Jack & Jones T-shirt    : £7  |")
    print("| Nike T-shirt            : £15 |")
    print("---------------------------------")
    print("\n")
    buy = input("Would you like to purchase an item: ")
    if buy == "yes".capitalize():
        purch = input("Please select one of the items: ")
        if purch == "underarmour".capitalize() or "underarmour t-shirt".capitalize():
            if main_menu.balance < 9:
                noBal()
            else:
                main_menu.balance - 9
                print("You have purchased Underarmour T-shirt")
                time.sleep(1)
                print("Your total balance is now:", main_menu.balance)
                Tshirt()
        if purch == "multipack".capitalize() or "t-shirt multipack".capitalize():
            if main_menu.balance < 18:
                noBal()
            else:
                main_menu.balance - 18
                print("You have purchased T-shirt multipack (1x5)")
                time.sleep(1)
                print("Your total balance is now:", main_menu.balance)
        if purch == "jack & jones".capitalize() or "jack & jones t-shirt".capitalize():
            if main_menu.balance < 7:
                noBal()
            else:
                main_menu.balance - 7
                print("You have purchased Jack & Jones T-shirt")
                time.sleep(1)
                print("Your total balance is now:", main_menu.balance)
        if purch == "nike".capitalize() or "nike t-shirt".capitalize():
            if main_menu.balance < 15:
                noBal()
            else:
                main_menu.balance - 15
                print("You have purchased Nike T-shirt")
                time.sleep(1)
                print("Your total balance is now:", main_menu.balance)
    if buy == "yes".capitalize():
        print("\n")
        print("-------------------------------")
        print("| Redirecting to home page... |")
        print("-------------------------------")
        time.sleep(1)
        main_menu.home_menu()
    else:
        print("Invalid data: Please try again")
        Tshirt()

def trouser():
    print("\n")
    print("|      Trousers      |")
    print("----------------------")
    print("| Jack & Jones : £20 |")
    print("| Levi's       : £35 |")
    print("| Under armour : £25 |")
    print("| Nike         : £18 |")
    print("----------------------")
    buy = input("Would you like to purchase an item: ")
    if buy == "yes".capitalize():
        purch = input("Please select one of the items: ")
        if purch == "jack and jones".capitalize() or "jack & jones".capitalize():
            if main_menu.balance < 20:
                noBal()
            else:
                main_menu.balance - 20
                print("You have purchased Jack & Jones trousers")
                time.sleep(1)
                print("Your total balance is now:", main_menu.balance)
                trouser()
        if purch == "levi's".capitalize() or "levis".capitalize():
            if main_menu.balance < 35:
                noBal()
            else:
                main_menu.balance - 35
                print("You have purchased Levi's trousers")
                time.sleep(1)
                print("Your total balance is now:", main_menu.balance)
                trouser()
        if purch == "under armour".capitalize():
            if main_menu.balance < 25:
                noBal()
            else:
                main_menu.balance - 25
                print("You have purchased Under Armour trousers")
                time.sleep(1)
                print("Your total balance is now:", main_menu.balance)
                trouser()
        if purch == "nike".capitalize():
            if main_menu.balance < 18:
                noBal()
            else:
                main_menu.balance - 18
                print("You have purchased Nike trousers")
                time.sleep(1)
                print("Your total balance is now:", main_menu.balance)
        else:
            print("Please enter a correct item")
            time.sleep(1)
            trouser()
    if buy == "no".capitalize():
        print("\n")
        print("-------------------------------")
        print("| Redirecting to home page... |")
        print("-------------------------------")
        time.sleep(1)
        main_menu.home_menu()
    else:
        print("Invalid data: Please try again")
        time.sleep(1)
        trouser()

def shoes():
    print("\n")
    print("|       Shoes        |")
    print("----------------------")
    print("| Puma         : £45 |")
    print("| Adidas       : £35 |")
    print("| New balance  : £25 |")
    print("| Vans         : £20 |")
    print("----------------------")
    buy = input("Would you like to purchase an item: ")
    if buy == "yes".capitalize():
        purch = input("Please select one of the items: ")
        if purch == "puma".capitalize():
            if main_menu.balance < 45:
                noBal()
            else:
                main_menu.balance - 45
                print("You have purchased Puma shoes")
                time.sleep(1)
                print("Your total balance is now:", main_menu.balance)
                shoes()
        if purch == "adidas".capitalize():
            if main_menu.balance < 35:
                noBal()
            else:
                main_menu.balance - 35
                print("You have purchased Adidas shoes")
                time.sleep(1)
                print("Your total balance is now:", main_menu.balance)
                shoes()
        if purch == "new balance".capitalize():
            if main_menu.balance < 25:
                noBal()
            else:
                main_menu.balance - 25
                print("You have purchased New balance shoes")
                time.sleep(1)
                print("Your total balance is now:", main_menu.balance)
                shoes()
        if purch == "vans".capitalize():
            if main_menu.balance < 20:
                noBal()
            else:
                main_menu.balance - 20
                print("You have purchased Vans shoes")
                time.sleep(1)
                print("Your total balance is now:", main_menu.balance)
                shoes()
        else:
            print("Please enter a correct item")
            time.sleep(1)
            shoes()

    if buy == "no".capitalize():
        print("\n")
        print("-------------------------------")
        print("| Redirecting to home page... |")
        print("-------------------------------")
        time.sleep(1)
        main_menu.home_menu()
    else:
        print("Invalid data: Please try again")
        time.sleep(1)
        shoes()
    

def clothing():
    print("\n")
    print("|         Clothing           |")
    print("------------------------------")
    print("| T-shirt | Trousers | Shoes |")
    print("------------------------------")
    print("\n")
    choice = input("")
    if choice == "t shirt".capitalize() or "t-shirt".capitalize():
        Tshirt()
    if choice == "trousers".capitalize():
        trouser()
    if choice == "shoes".capitalize():
        shoes()
    else:
        print("Invalid data: Please try again")
        time.sleep(1)
        clothing()

