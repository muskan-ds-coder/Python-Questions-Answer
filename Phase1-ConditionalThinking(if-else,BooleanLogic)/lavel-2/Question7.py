# Take two numbers and determine whether both are even, both are odd, or one is even and one is odd.

num1 = int(input("Enter a number:- "))
num2 = int(input("Enter a number:- "))

if num1 %  2 == 0 and num2 % 2 == 0:
    print("both are even")
elif num1 % 2 != 0 and num2 % 2 != 0:
    print("both are odd")
else:
    print("one is even and one is odd")

