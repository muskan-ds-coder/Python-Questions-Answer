# print the factorial of a given number.

n = int(input("enter a number:- "))

fact = 1
for i in range(1, n):
    fact *= (n - i + 1) 
print(f"factorial of {n} = ", fact)