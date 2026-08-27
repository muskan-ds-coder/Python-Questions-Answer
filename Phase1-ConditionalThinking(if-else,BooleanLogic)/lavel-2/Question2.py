# if the sides form a valid triangle , determine whether it is equilteral, isosceles, or scalene.

side1 = int(input("enter a number"))
side2 = int(input("enter a number"))
side3 = int(input("enter a number")) 

if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2:
    if side1 == side2 and side2 == side3:
        print("equilteral")
    elif side1 == side2:
        print("issosceles")
    else:
        print("scalene")
else:
    print("not valid")

