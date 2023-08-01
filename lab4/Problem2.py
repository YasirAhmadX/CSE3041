#1st August (Problem 2 palindrome) 22MIA1064 Yasir Ahmad

s = input("Enter string:")

print("Palindrome" if s.lower() == s[::-1].lower() else "Not Palindrome")
