#26th July (Problem 5 Fibonanci sequence using while) 22MIA1064 Yasir Ahmad

a = 0
b = 1

n = int(input("Enter n: "))
i=1

while i<=n:
    if i==1:
        print(a)
    elif i==2:
        print(b)
    else:
        c = a+b
        a = b
        b = c
        print(c)
    i +=1    
