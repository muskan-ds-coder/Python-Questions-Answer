# Check if an amountn can be evenly divided into 2000, 500 and 100 currency notes.
amount = int(input("Enter an amount: "))
if amount % 2000 == 0:
    print(" evenly divided by 2000 .")
elif amount % 500 == 0:
    print(" evenly divided by 500 .")
elif amount % 100 == 0:
    print(" evenly divided by 100 .")
else:
    print(" cannot be evenly divided.")