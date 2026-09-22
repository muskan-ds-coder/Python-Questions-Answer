# 2. Take three numbers and check if they can form a Pythagorean triplet. 

num1 = int(input("enter first number:-"))
num2 = int(input("enter second number:-"))
num3 = int(input("enter third number:-"))

if num1 >= num2 and num1 >= num3:
    largest = num1
    other1 = num2
    other2 = num3
elif num2 >= num1 and num2 >= num3:
    largest = num2
    other1 = num1
    other2 = num3
else:
    largest = num3 
    other1 = num1
    other2 = num2

if other1**2 + other2**2 == largest**2:
    print("Pythagorean triplet")
else:
    print("Not a Pythagorean triplet")



