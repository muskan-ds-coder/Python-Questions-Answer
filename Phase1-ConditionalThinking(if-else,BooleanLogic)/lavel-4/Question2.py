# Take a number and check "Fizz" if divisible by 3, and "Buzz" if divisible by 5 and "FizzBuzz" if divisible by both 3 and 5.

num = int(input("enter a number:-"))

if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 5 == 0:
    print("Buzz")
elif num % 3 == 0:
    print("Fizz")
else:
    print("No match")