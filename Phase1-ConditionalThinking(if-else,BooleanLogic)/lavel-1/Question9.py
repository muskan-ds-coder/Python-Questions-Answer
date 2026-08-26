# take a characterand check if it's a vowel or consonant.

char = input("Please enter a character :- ")
if char in 'aeiouAEIOU':
    print(f"{char} is vowel")
else:
    print(f"{char} is not vowel")