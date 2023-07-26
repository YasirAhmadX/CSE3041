#26th July (Problem 4 factorial using while) 22MIA1064 Yasir Ahmad

n = int(input("Enter n: "))
fact = 1
while n>1:
    fact *= n
    n -= 1

print("n! =",fact)
