#1st August (Problem 1 count number of vowels) 22MIA1064 Yasir Ahmad

s = input("Enter string: ")
count = 0
for i in s.lower():
    if i in "aeiou":
        count += 1

print("Number of vowels:",count)
