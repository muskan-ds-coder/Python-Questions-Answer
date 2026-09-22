# Take a 4 digit number and check if the first and last digit are equal

num = int(input("Enter a 4 digit number: "))

first_digit = num // 1000
last_digit = num % 10

if first_digit == last_digit:
    print("first and last digit are equal")
else:
    print("first and last disgit are not equal")