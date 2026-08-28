# Take the hour of the day (0-23) and print good morning, good afternoon, good evening, or good night

hour = int(input("enter your time:- "))

if hour < 12:
    print("Good Morning")
elif hour < 16:
    print("Good Afternoon")
elif hour < 20:
    print("Good Evening")
elif hour < 24:
    print("Good Night")
