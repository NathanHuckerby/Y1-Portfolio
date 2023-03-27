#asks the user how many places they want to be generated
places = int(input("How many places would you like to generate?"))

#first 2 terms that will be displayed in the generated sequence
n1 = 0
n2 = 1
#counts how many times each number is generated
count = 0

if places <= 0:
    print("Please input a positive number")
else:
    print("Fibonacci sequence up to", places, "places:")
    #generats the fibonacci sequence to the user's place
    while count < places:
        print(n1)
        next = n1 + n2
        #updates the variables so the fibonacci sequence is generated
        n1 = n2
        n2 = next
        count += 1
