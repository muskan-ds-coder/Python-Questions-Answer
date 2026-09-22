# 8. Take an integer (1–9999) and check if the sum of its digits is greater than the product of its digits. 

num = int(input("Enter an integer (1–9999): "))

# Extract individual digits
digit1 = num // 1000
digit2 = num // 100 % 10
digit3 = num // 10 % 10
digit4 = num % 10

# Calculate sum and product of digits
sum_of_digits = digit1 + digit2 + digit3 + digit4
product_of_digits = digit1 * digit2 * digit3 * digit4

# Check the condition
if sum_of_digits > product_of_digits:
    print("The sum of the digits is greater than the product of the digits.")
else:
    print("The sum of the digits is not greater than the product of the digits.")