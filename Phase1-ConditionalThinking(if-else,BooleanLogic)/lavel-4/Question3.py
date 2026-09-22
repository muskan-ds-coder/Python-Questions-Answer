# Take three numbers and print the median value (neither maximum nor minimum)

num1 = int(input("enter first number:-"))
num2 = int(input("enter second number:-"))
num3 = int(input("enter third number:-"))

if (num1 > num2 and num1 < num3) or (num1 < num2 and num1 > num3):
    print("median:", num1)
elif (num2 > num1 and num2 < num3) or (num2 < num1 and num2 > num3):
    print("median:", num2)
elif (num3 > num1 and num3 < num2) or (num3 < num1 and num3 > num2):
    print("median:", num3)
else:
    print("neither maximum nor minimum")
    