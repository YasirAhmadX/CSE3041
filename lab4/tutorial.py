#1st August (Tutorial basic stringops) 22MIA1064 Yasir Ahmad

s = input("Enter name:")

print("Length:",len(s))
print("Lower case:",s.lower())
print("Upper case:",s.upper())


sumOfASCII = sum([ord(i) for i in s])
print("Sum of ASCII:",sumOfASCII)


print("Count of 'b':",s.count('b'))
