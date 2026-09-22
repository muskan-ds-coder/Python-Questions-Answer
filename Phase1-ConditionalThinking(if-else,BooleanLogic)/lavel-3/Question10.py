# check whether a number is a perfect square (without using the square root function)

num = int(input("Enter a number:- "))

is_square = False

for i in range(1, num + 1):
    if i * i == num:
        is_square = True
        break

if is_square:
    print("perfect square")
else:
    print("not a perfect square")