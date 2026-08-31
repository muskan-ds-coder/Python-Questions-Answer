# find the square root

num1 = int(input("Enter a number:- "))
num2 = int(input("Enter a number:- "))

sr = num1**(1/2)
sr1 = num2**(1/2)

print(f"the square root of the given number {sr} and {sr1}")


# using math module
import math

sr2 = math.sqrt(num1)
sr3 = math.sqrt(num2)

print(f"the square root of the given number {sr2} and {sr3}")