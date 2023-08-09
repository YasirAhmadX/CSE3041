#9th August (Problem 6 tuples x%5=0) 22MIA1064 Yasir Ahmad

t = ()
for i in range(int(input("Enter N: "))):
    t += (int(input()),)

k = ()

for j in t:
    if j%5==0:
        k += (j,)

print(f"Given tuple T={t}\nMultiples of 5: K={k}")
