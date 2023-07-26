#26th July (Problem 1 reverse and diff) 22MIA1064 Yasir Ahmad

n = int(input())
rn = 0

b = n
while b>0:
    rn *= 10
    rn += b%10
    b = b//10

print(abs(n-rn))

"""
n = input()
rn = n[::-1] #reverse string

n = int(n)
rn = int(rn)

print(abs(n-rn))
"""
