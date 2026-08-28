# check if one of two givin number is a multiple of the other

num1 = int(input("enter a number:- "))
num2 = int(input("enter a number:- "))

if num1 % num2 == 0 or num2 % num1== 0:
    print("One number is a multiple of the other")
else:
    print("Neither number is a multiple of the other")