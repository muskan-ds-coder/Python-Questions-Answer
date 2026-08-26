# take a temperature value and print "cold", "warm", or "hot"range conditions.

temp = int(input("Please enter your temperature :- "))

if temp <= 20:
    print("cold")
elif temp <= 40:
    print("warm")
else:
    print("hot")