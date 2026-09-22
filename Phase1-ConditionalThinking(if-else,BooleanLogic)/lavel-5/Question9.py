# 9. Take two dates (day and month) and determine which one comes first in the calendar. 

date1_day = int(input("Enter the day for the first date: "))
date1_month = int(input("Enter the month for the first date: "))

date2_day = int(input("Enter the day for the second date: "))
date2_month = int(input("Enter the month for the second date: "))

if date1_month < date2_month:
    print(f"The first date comes first.{date1_day}, {date1_month}")
elif date1_month > date2_month:
    print(f"The second date comes first.{date2_day}, {date2_month}")
else:
    if date1_day < date2_day:
        print(f"The first date comes first.{date1_day}, {date1_month}")
    elif date1_day > date2_day:
        print(f"The second date comes first.{date2_day}, {date2_month}")
    else:
        print(f"Both dates are the same.")