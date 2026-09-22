# Take 24 hour time (hours and minutes) and print whether it is AM or PM

hour = int(input("enter your hour :- "))
minutes = int(input("enter your minutes:- "))
if (hour >= 0 and minutes >= 0) and (hour <= 11 and minutes <= 59):
    print("AM")
elif (hour >= 12 and minutes >= 0) and (hour <= 23 and minutes <= 59):
    print("PM")
else:
    print("please enter your correct time")

# hour = int(input("enter your hour :- "))
# minutes = int(input("enter your minutes:- "))
# if ((hour >= 0 and minutes >= 0) and (hour <= 11 and minutes <= 59)) or ((hour >= 24 and minutes >= 0) and (hour <= 35 and minutes <= 59)):
#     print("AM")
# elif ((hour >= 12 and minutes >= 0) and (hour <= 23 and minutes <= 59)) or ((hour >= 36 and minutes >= 0) and (hour <= 47 and minutes <= 59)):
#     print("PM")
# else:
#     print("please enter your correct time")