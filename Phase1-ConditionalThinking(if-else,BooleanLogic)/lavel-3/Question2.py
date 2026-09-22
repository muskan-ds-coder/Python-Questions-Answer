# Take a 3 digit number and determine if the middle digit is the largest smallest, or neither.

number = int(input("Enter a 3 digit number:- "))

first = number // 100
middle = (number // 10) % 10
last = number % 10

if middle > first and middle > last:
    print("Middle digit is the largest.")
elif middle < first and middle < last:
    print("Middle digit is the smallest.")
else:
    print("Middle digit is neither the largest nor the smallest.")