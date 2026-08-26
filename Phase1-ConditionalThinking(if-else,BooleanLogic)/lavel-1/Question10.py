# Take a character and check whether it's uppercase, lowercase, a digit, or a special character

char = input("enter a character:- ")

if char.isupper():
    print("uppercase")
elif char.islower():
    print("lowercase")
elif char.isdigit():
    print("digit")
else:
    print("special character")