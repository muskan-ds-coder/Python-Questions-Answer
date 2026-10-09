# Print the sum of all odd numbers up to n

n = int(input("enter a number: "))
sum_odd = 0
for i in range(1, n + 1, 2):
    sum_odd += i

print(f"sum of odd number up to {n} is: {sum_odd}")