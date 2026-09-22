# Take two numbers and check if both are positive and their sum is less than 100.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > 0 and num2 > 0 and (num1 + num2) < 100:
    print("Both numbers are positive and their sum is less than 100.")
elif num1 > 0 and num2 > 0:
    print("Both numbers are positive but their sum is 100 or more.")
else:
    print("Either one or both numbers are not positive or their sum is 100 or more.")