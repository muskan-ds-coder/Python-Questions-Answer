# check leap year

year = int(input("Enter a number:- "))

if (year % 400 == 0) and (year % 100 == 0):
    print("Leap year")
elif (year % 4 == 0) and (year % 100 != 0):
    print("leap year")
else:
    print("Not leap year")