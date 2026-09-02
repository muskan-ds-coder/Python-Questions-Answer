# chek if a given year is a leap year.

num = int(input("Enter a year number :- "))

if (num % 400 == 0) and (num % 100 == 0):
    print("leap year ")
elif(num % 4 == 0 ) and (num % 100 != 0):
    print("leap year")
else:
    print("not leap year ")