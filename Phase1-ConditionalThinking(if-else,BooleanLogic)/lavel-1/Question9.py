# take a character and check if it's a vowel or consonant.

# char = input("Please enter a character :- ")
# if char in 'aeiouAEIOU':
#     print(f"{char} is vowel")
# elif char in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
#     print(f"{char} is consonant")
# else:
#     print("please enter alphabate character")


char = input("Please enter a character :- ")
if char in 'aeiouAEIOU':
    print(f"{char} is vowel")
elif ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
    print(f"{char} is consonant")
else:
    print("please enter alphabate character")