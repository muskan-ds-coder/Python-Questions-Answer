# Print the table of a given number (n * 1 to n * 10)
n = int(input("Enter a table number: "))

for i in range(1, 11):
    print(f"{n} * {i} = {n * i}")