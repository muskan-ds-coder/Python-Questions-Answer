# check if is a multiple of 7 or end with 7

num = int(input("Enter an integer: "))

if num % 7 == 0 or num % 10 == 7:
    print("The number is a multiple of 7 or ends with 7")
else:
    print("The number is not a multiple of 7 and does not end with 7")