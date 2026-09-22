# 6. Take three numbers and check if they are in geometric progression. 

num1 = int(input("enter first number:-"))
num2 = int(input("enter second number:-"))
num3 = int(input("enter third number:-"))

# if num1 != 0 and num2 != 0:
#     first = num2 / num1 
#     second = num3 / num2

#     if first == second:
#         print("geometric progression")
#     else:
#         print("not geometric progression")


if num1 != 0 and num2 != 0:
    if (num2 / num1) == (num3 / num2):
        print("Geometric progression")
    else:
        print("not geometric progression")
else:
  print("not geometric progression")

