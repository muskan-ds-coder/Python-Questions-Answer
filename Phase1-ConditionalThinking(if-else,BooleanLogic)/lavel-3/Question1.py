# // Math and number logic //

# Take a 3 digit number and check if all digits are distinct.

num = int(input("Enter a 3 digit number:- "))

# Extract the hundreds, tens, and units digits
hundreds = num // 100
tens = (num // 10) % 10
units = num % 10

# Check if all digits are distinct
if hundreds != tens and hundreds != units and tens != units:
    print("All digits are distinct.")
else:
    print("Not all digits are distinct.")
