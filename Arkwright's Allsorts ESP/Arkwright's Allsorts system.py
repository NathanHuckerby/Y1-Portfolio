import csv
system_list = []

def write():
        with open("system_list.txt", "w") as file:
                file.write(str(system_list) + '\n')
                file.close()

def write2(data):
        with open("system_list.txt", "w") as file:
                file.write(str(data))
                file.close()
                
def read():
        with open('system_list.txt', 'r') as file:
                lines = []
                for line in file:
                        lines.append(line.rstrip())
                return lines
def getdata():
        with open('system_list.txt', 'r') as file:
                lines = []
                for line in file:
                        lines.append(eval(line.rstrip()))
                return lines                
        
def append():
        with open('system_list.txt', 'a') as file:
                file.write(str(system_list) + '\n')
                file.close()
                
def append2(data):
        with open('system_list.txt', 'a') as file:
                file.write(str(data) + '\n')
                file.close()        

productNumber = ()
def new():
        productName = input("What is the product's name?")
        system_list.append(productName)
        productID = int(input("What is the product's ID?"))
        system_list.append(productID)
        productDep = input("What is the product's department?")
        system_list.append(productDep)
        productLocation = input("Where is the product located?")
        system_list.append(productLocation)
        priceVAT = float(input("What is the price of the product inc VAT?"))
        system_list.append(priceVAT)
        priceEx_VAT = float(input("What is the price of the product exc VAT?"))
        system_list.append(priceEx_VAT)
        Stock = int(input("What is the amount of stock of the product?"))
        system_list.append(Stock)
        print(system_list)


def menu():
        print("------------------------------------------------")
        print("Welcome to Arkwright's Allsorts Tracking system")
        print("Please choose from one of the following options:")
        print("A. Search by product ID")
        print("B. Search by product name")
        print("C. Add a new product")
        print("D. Remove a product from the system")
        print("E. Change stock of product")
        print("F. Exit the system")
        
while True:

        menu()

        option = input("I would like to choose option: ")

        if option.lower() == "c":
            new()
            append()

        if option.lower() == "a":
                productID = int(input("Please enter the product's ID "))
                for item in read():
                        if eval(item)[1] == productID:
                                print(eval(item))
                                break
                        
        if option.lower() == "d":
                productID = int(input("Please enter the product's ID "))
                data = getdata()
                for item in data:
                        if item[1] == productID:
                                data.remove(item)
                                write2("")
                                break
                for item in data:
                        append2(item)
        if option.lower() == "b":
                productName = input("Please enter the product's name ")
                for item in read():
                        if eval(item)[0] == productName:
                                print(eval(item))
                                break
        if option.lower() == "e":
                productName = input("What is the product's name? ")
                amount = int(input("How much do you want to change it by ( - for decrease in stock) "))
                data = getdata()
                for item in data:
                        if item[0] == productName:
                                item[6] += amount
                                write2("")
                                break
                for item in data:
                        append2(item)
                        
        if option.lower() == "f":
                break                     
        
        
    





