# 5. Take three numbers and check if they are in arithmetic progression. 

num1 = int(input("enter first number:-"))
num2 = int(input("enter second number:-"))
num3 = int(input("enter third number:-"))

# first = num2 - num1 
# second = num3 - num2

# if first == second:
#   print("arthmetic progression")
# else:
#   print("not arthmetic progression")


if (num2 - num1) == (num3 - num2):
    print("The numbers are in arithmetic progression")
else:
    print("The numbers are not in arithmetic progression")