# check whether a given integer is single digit, double digit or multi digit.

num = int(input("Enter an integer: "))

if num < 10:
    print("single digit")
elif num < 100:
    print("double digit")
else:
    print("multi digit")