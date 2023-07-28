#28th July (Problem 5 prime) 22MIA1064 Yasir Ahmad

n = int(input("Enter n: "))

p = True

for i in range(2,n):
    if(n%i ==0):
        p=False
        break
    
print("Prime" if (p and n>1)  else "Not Prime")
