import secrets
import string

#Grab all letter of the alphabet, numbers 0-9, and symbols

char = string.ascii_letters + string.digits + string.punctuation

length = int(input("Length of password: "))

#chose random characters using secrets and including the length

password = "".join(secrets.choice(char) for i in range(length))

#Makes sure they is atleast 1 upper case and 1 lower case letter in password

if(any(c.islower and c.isupper) for c in password):    
    print(f"your password is, {password}")

