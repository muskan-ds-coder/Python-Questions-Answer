# Take income and age, and check if aligible for tax (age >18 and income > 5L).

age = int(input("enter your age:- "))
income = int(input("enter your income:- "))

if age > 18 and income > 500000:
    print("aligible for tax")
else:
    print ("not aligble for tax")