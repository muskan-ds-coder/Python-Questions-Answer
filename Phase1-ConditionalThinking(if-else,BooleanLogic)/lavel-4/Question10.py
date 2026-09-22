# Take a password string and check basic rules (length ≥ 8 and contains at least one digit)

password = input("Enter a password: ")

has_digit = False

for char in password:
    if char.isdigit():
        has_digit = True
        break

if len(password) >= 8 and has_digit:
    print("valid password")
else:
    print("Invalid password")
