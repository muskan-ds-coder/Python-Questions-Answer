# Take a weekday number (1–7) and determine if it is a weekday or weekend. 

num = int(input("enter a number(1-7):- "))

if num == 1 or num == 2 or num == 3 or num == 4 or num == 5:
    print("weekday")
elif num == 6 or num == 7:
    print("weekend")
else:
    print("invalid weekday number")