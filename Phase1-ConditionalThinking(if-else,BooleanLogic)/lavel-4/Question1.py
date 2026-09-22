## Logical Operators & Compound Statements

# Take a character and check if is a letter, a digit, or nether.

char = input("Enter a character:- ")

if char.isalpha():
    print("The character is a letter.")
elif char.isdigit():
    print("The character is a digit.")
else:
    print("The character is neither a letter nor a digit.")