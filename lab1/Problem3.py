#25th July (Problem 3 Bob and chocolates) 22MIA1064 Yasir Ahmad

"""
Bob has Rs. N
Each chocolates cost Rs. C
On returning M wrappers, the shopkeeper gives 1 chocolate free.

How many chocolates can Bob have.
"""

n = int(input("Enter n:"))
c = int(input("Enter c:"))
m = int(input("Enter m:"))


choco = n//c + (n//c)//m

print("Chocolates:",choco)

