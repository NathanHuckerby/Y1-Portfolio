#checks the reverse of the string inputted
def palindrome(user):
    return user == user[::-1]

#user enters their word. If it is a palidrome, the program will say "Yes it is". If not, the program will say "No it is not"
print("Please enter your word")
user = input("")
check = palindrome(user)

if check:
    print("Yes it is")
else:
    print("No it is not")