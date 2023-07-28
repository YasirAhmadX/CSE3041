#28th July (Problem 4 GCD) 22MIA1064 Yasir Ahmad

m = int(input("Enter M: "))
n = int(input("Enter N: "))

for i in range(min(m,n),0,-1):
    if(m%i==0 and n%i==0):
        print("Number of boxes(HCF):",i)
        break
