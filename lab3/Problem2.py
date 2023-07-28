#28th July (Problem 2 factors) 22MIA1064 Yasir Ahmad

n = int(input("Enter n: "))
print("Factors :",end=" ")
for i in range(1,n+1):
    if n%i==0:
        print(i,end=" ")
