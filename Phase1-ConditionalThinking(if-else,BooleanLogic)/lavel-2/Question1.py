#     lavel-2: Nasted if & Multiple Condition
# Take three sides and check if they form a valid triangle.

side1 = int(input("enter a number"))
side2 = int(input("enter a number"))
side3 = int(input("enter a number"))

if side1 + side2 > side3 and side2 +side3 > side1 and side1 + side3 > side2:
    print("valid triangle")
else:
    print("invalid triangle")