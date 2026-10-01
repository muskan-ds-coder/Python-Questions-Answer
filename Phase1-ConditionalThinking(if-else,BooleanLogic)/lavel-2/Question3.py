# Take marks (0-100) and print corresponding grade (A, B, C, D, F).

marks = int(input("enter your marks:- "))

if marks >= 80 and marks <= 100:
    print("Grade:- A")
elif marks >= 60 and marks < 80:
    print("Grade:- B")
elif marks >= 50 and marks < 60:
    print("Grade:- C")
elif marks >= 40 and marks < 50:
    print("Grade:- D")
else:
    print("Grade:- F")