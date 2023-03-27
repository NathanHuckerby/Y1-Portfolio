#Used to create passwords
import secrets
#Formats into string type
import string

#assign letters, numbers, and special characters into variables
letters=string.ascii_letters
digits=string.digits
special_characters=string.punctuation

#assigns the letters, digits, and special characters into one variable
list = letters + digits + special_characters

#sets the password length
pwd_length = 8

#where the generated password will be stored
pwd = ''

#generates the random code from the list
for i in range(pwd_length):
    pwd += ''.join(secrets.choice(list))
#the secrets.choice(list) returns one random character from the list, so the loop continuously repeats the process until the password reaches 8 characters
#the join() method is used to add the random character generated to the pwd variable.
print(pwd)