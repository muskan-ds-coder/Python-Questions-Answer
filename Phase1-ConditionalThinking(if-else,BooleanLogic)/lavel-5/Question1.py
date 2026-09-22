# 1. Take coordinates (x, y) and check if the point lies on the X-axis, Y-axis, or at the origin. 

x = float(input("Enter the x-coordinate: "))
y = float(input("Enter the y-coordinate: "))

if x == 0 and y == 0:
    print("The point is at the origin")
elif x == 0:
    print("The point lies on the X-axis")
elif y == 0:
    print("The point lies on the y-axis")
else:
    print("Please enter valid ")