from random import choice, randint, sample
import time

#program will ask the user to enter 4 digits that they already know. This will be used to generate the PIN

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))
num4 = int(input("Enter 4th number: "))

#puts the numbers into a separate array, which will be used later
PIN = [num1, num2, num3, num4]

#this code will generate the correct PIN using the numbers inputted by the user

generated_pin = sample(PIN, len(PIN))
time.sleep(1)

#displays the correct PIN sequence to the user
print("The correct PIN is:" + str(generated_pin))