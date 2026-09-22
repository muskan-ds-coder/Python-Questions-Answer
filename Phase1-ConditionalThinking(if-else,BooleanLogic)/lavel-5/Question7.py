# 7. Take a 3-digit number and check if the sum of the first and last digit equals the middle digit.

num = int(input("Enter a 3-digit number: "))

first = num // 100
middle = num // 10 % 10
last = num % 10 

if first + last == middle:
    print("The sum of the first and last digit equals the middle digit.")
else:
    print("first and last digit are not equals")
    