# Take electricity units consumed and calculate the bill as per slabs (using if-else). 

units = int(input("enter electricity units:- "))

# per_unit_slabs = int(input("enter per unit slabs:- "))
# bill = units * per_unit_slabs
# print(bill)

if units <= 300:
    bill = units * 10
elif units <= 200:
    bill = units * 7
elif units <= 100:
    bill = units * 5
else:
    bill = units * 15

print("Electricity bill:" , bill )