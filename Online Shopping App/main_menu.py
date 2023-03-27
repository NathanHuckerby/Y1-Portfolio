import Digital
import time
import Lifestyle

def noBal():
    print("Unable to purchase item: Insufficient funds")
    home_menu()


balance = 2000

def digital():
        print("\n")
        print("           Digtal            ")
        print("-----------------------------")
        print("|   Gaming    |   Phones    |")
        print("-----------------------------")
        print("\n")


def categories():
        print("\n")
        print("|                        Categories                                   |")
        print("-----------------------------------------------------------------------")
        print("| Digital | Music | Lifestyle | Gardening | Books | Clothing | Sports |")
        print("-----------------------------------------------------------------------")
        print("|                            Back                                     |")
        print("\n")


def home_menu():
    print("|                      Shopping4You                          |")
    print("--------------------------------------------------------------")
    print("|      Home page     |    Categories   |     Latest deals    |")
    print("--------------------------------------------------------------")
    print("|                      Balance:                               ", balance)
    print("\n")
    type = input("")

    if type == "home page".capitalize():
        home_menu()
    if type == "categories".capitalize():
        categories()
        type2 = input("")
        
        if type2 == "digital".capitalize():
            digital()
            dig = input("")
            if dig == "gaming".capitalize():
                Digital.gaming()
            if dig == "phones".capitalize():
                Digital.phones()
        
        if type2 == "music".capitalize():
            print("\n")
            print("|     Music     |")
            print("-----------------")
            print("| Drums  : £50  |")
            print("| Guitar : £70  |")
            print("| Piano  : £20  |")
            print("| Violin : £40  |")
            print("-----------------")
            buy = input("Would you like to purchase an item: ")
            if buy == "yes".capitalize():
                purch = input("Please select one of the items: ")
                if purch == "drums".capitalize():
                    if balance < 50:
                        noBal()
                    else:
                        balance - 50
                        print("You have purchased Drums")
                        time.sleep(1)
                        print("Your total balance is now:", balance)
                        categories()
                if purch == "guitar".capitalize():
                    if balance < 70:
                        noBal()
                    else:
                        balance - 70
                        print("You have purchased Guitar")
                        time.sleep(1)
                        print("Your total balance is now:", balance)
                        categories()
                if purch == "piano".capitalize():
                    if balance < 20:
                        noBal()
                    else:
                        balance - 20
                        print("You have purchased Piano")
                        time.sleep(1)
                        print("Your total balance is now:", balance)
                        categories()
                if purch == "violin".capitalize():
                    if balance < 40:
                        noBal()
                    else:
                        balance - 40
                        print("You have purchased Violin")
                        time.sleep(1)
                        print("Your total balance is now:", balance)
                        categories()
            if buy == "no".capitalize():
                print("\n")
                print("-------------------------------")
                print("| Redirecting to home page... |")
                print("-------------------------------")
                time.sleep(1)
                home_menu()
        if type2 == "lifestyle".capitalize():
            Lifestyle.lifestyle()
        if type2 == "gardening".capitalize():
            print("\n")
            print("|      Gardening       |")
            print("------------------------")
            print("| Lawnmower     : £100 |")
            print("| Hedge Trimmer : £80  |")
            print("| Rose bush     : £40  |")
            print("| Garden shed   : £200 |")
            print("------------------------")
            buy = input("Would you like to purchase an item: ")
            if buy == "yes".capitalize():
                purch == ("Please select one of the items: ")
                if purch == "lawnmower".capitalize():
                    if balance < 100:
                        noBal()
                    else:
                        balance - 100
                        print("You have purchased Lawnmower")
                        time.sleep(1)
                        print("Your total balance is now:", balance)
                        categories()
                if purch == "hedge trimmer".capitalize():
                    if balance < 80:
                        noBal()
                    else:
                        balance - 80
                        print("You have purchased Hedge Trimmer")
                        time.sleep(1)
                        print("Your total balance is now:", balance)
                        categories()
                if purch == "rose bush".capitalize():
                    if balance < 40:
                        noBal()
                    else:
                        balance - 40
                        print("You have purchased Rose bush")
                        time.sleep(1)
                        print("Your total balance is now:", balance)
                        categories()
                if purch == "garden shed".capitalize():
                    if balance < 200:
                        noBal()
                    else:
                        balance - 200
                        print("You have purchased Garden shed")
                        time.sleep(1)
                        print("Your total balance is now:", balance)
                        categories()
            if buy == "no".capitalize():
                print("\n")
                print("-------------------------------")
                print("| Redirecting to home page... |")
                print("-------------------------------")
                time.sleep(1)
                home_menu()
            else:
                print("Invalid data: Please try again")
                time.sleep(1)
                home_menu()

        if type2 == "books".capitalize():
            print("\n")
            print("|                  Books                      |")
            print("-----------------------------------------------")
            print("| Harry Potter & The Chamber of Secrets : £12 |")
            print("| The Very Hungry Caterpilla            : £4  |")
            print("| Doctor Sleep                          : £9  |")
            print("| The Lord of The Rings                 : £6  |")
            print("-----------------------------------------------")
            buy = input("Would you like to buy an item: ")
            if buy == "yes".capitalize():
                purch = input("Please select an item: ")
                if purch == "harry potter".capitalize() or "chamber of secrets".capitalize():
                    if balance < 12:
                        noBal()
                    else:
                        balance - 12
                        print("You have purchased Harry Potter & The Chamber of Secrets")
                        time.sleep(1)
                        print("Your total balance is now:", balance)
                        categories()
                if purch == "the very hungry caterpilla".capitalize():
                    if balance < 4:
                        noBal()
                    else:
                        balance - 4
                        print("You have purchased The Very Hungry Caterpilla")
                        time.sleep(1)
                        print("Your total balance is now:", balance)
                        categories()
                if purch == "doctor sleep".capitalize():
                    if balance < 9:
                        noBal()
                    else:
                        balance - 9
                        print("You have purchased Doctor Sleep")
                        time.sleep(1)
                        print("Your total balance is now:", balance)
                        categories()
                if purch == "lord of the rings".capitalize() or "the lord of the rings".capitalize():
                    if balance < 6:
                        noBal()
                    else:
                        balance - 6
                        print("You have purchased The Lord of The Rings")
                        time.sleep(1)
                        print("Your total balance is now:", balance)
                        categories()
            if buy == "no".capitalize():
                print("\n")
                print("-------------------------------")
                print("| Redirecting to home page... |")
                print("-------------------------------")
                time.sleep(1)
                home_menu()
            else:
                print("Invalid data: Please try again")
                time.sleep(1)
                categories()

                

                    
