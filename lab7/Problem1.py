#9th August (Problem 1 list Supermarket ) 22MIA1064 Yasir Ahmad

"""
In a supermarket two list are maintained, having n and p items respectively.
WAP to get list_1 and list_2 , and merger them in sorted order
"""

s1 = []
s2 = []

for i in range(int(input("Enter n: "))):
    s1.append(input("Enter item in list_1: "))

for i in range(int(input("Enter p: "))):
    s2.append(input("Enter item in list_2: "))

s1.extend(s2)

s1.sort()

print(s1)
