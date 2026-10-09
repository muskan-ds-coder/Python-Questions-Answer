#print the sum all even number up to n

n = int(input("enter a number: "))
sum = 0
for i in range(2, n + 1, 2):
    sum += i

print(f"sum of even numbers up to {n} is: {sum}")


