# Find the factorial of a number.

number = int(input("Enter a number to find its factorial: "))
fact = 1

if number < 0:
    print("factorial of 0 does not exist")
if number == 0:
    print("The factorial of 0 is ", 1)
if number > 0:
    for i in range(1, number + 1):
        fact *= i
    print("The factorial of", number, "is", fact)


# solution 2 using recursion

def fact(a):
    if a == 0:
        return 1
    else:
        return a * fact(a - 1)

num = int(input("Enter a number to find its factorial: "))
result = fact(num)
print("The factorial of the given number is", result)

    
    