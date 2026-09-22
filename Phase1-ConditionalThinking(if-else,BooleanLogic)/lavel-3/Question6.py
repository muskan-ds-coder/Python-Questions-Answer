# Take  coordinates(x, y) and determine which quadrant the point lies in.

x = float(input("Enter x coordinate:-"))
y = float(input("Enter y coordinate:-"))

if x > 0 and y > 0:
    print("first quadrant")
elif x < 0 and y > 0:
    print("second quadrant")
elif x < 0 and y < 0:
    print("third quadrant")
elif x > 0 and y < 0:
    print("fourth quadrant")
else:
    print("The point lies on an axis")