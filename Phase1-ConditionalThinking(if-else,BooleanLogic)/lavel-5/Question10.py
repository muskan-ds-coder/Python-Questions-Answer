# 10. Take a year and print the corresponding century (e.g., “19th century”, “20th century”) 

year = int(input("Enter a year: "))

if year % 100 == 0:
    century = year // 100
else:
    century = year // 100 + 1

print(f"The year {year} corresponds to the {century}", end="")