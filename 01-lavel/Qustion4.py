#check if number is divisible by both 3 and 5.

num = int(input("Enter a number :- "))

if num % 3 and num % 5:
    print("not divisible 3 and 5")
else:
    print("divisible")