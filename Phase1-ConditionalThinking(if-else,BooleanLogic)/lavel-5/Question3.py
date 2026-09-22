# 3. Take day and month and check if it forms a valid calendar date (ignoring leap years).

day = int(input("Enter a day:- "))
month = int(input("Enter a month:- "))

# if (month == 2) and (day >= 1 and day <= 28):
#     print("valid calendar is", day ,":" , month)
# elif ((month == 4) or (month == 6) or (month == 9) or (month == 11)) and (day >= 1 and day <= 30):
#     print("valid calendar is", day ,":" , month)
# elif ((month == 1) or (month == 3) or (month == 5) or (month == 7) or (month == 8) or (month == 10) or (month == 12)) and (day >= 1 and day <= 31):
#     print("valid calendar is", day ,":" , month)
# else:
#     print("not valid calendar")

if month in [1, 3, 5, 7, 8, 10, 12]:
    if day >= 1 and day <= 31:
        print("valid calendar date")
    else:
        print("not valid")
elif month in [4, 6, 9, 11]:
    if day >= 1 and day <= 30:
        print("valid calendar date")
    else:
        print("not valid")
elif month == 2:
    if day >= 1 and day <= 28:
        print("valid calendar date")
    else:
        print("not valid")
else:
    print("not valid")