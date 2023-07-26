#26th July (Problem 10 reverse) 22MIA1064 Yasir Ahmad

n = int(input("Enter number: "))
rn = 0

b = n
while b>0:
    rn *= 10
    rn += b%10
    b = b//10

print("Enter reverse number:",rn)
