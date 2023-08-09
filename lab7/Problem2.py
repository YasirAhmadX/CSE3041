#9th August (Problem 2 sort without builtin ) 22MIA1064 Yasir Ahmad

l = []

for i in range(int(input("Enter n: "))):
    l.append(int(input("Enter item {0}: ".format(i+1))))

print(f"Original list l: {l}")
#selection sort
for i in range(len(l)):
    m = i
    for j in range(i,len(l)):
        if l[j] < l[m]:
            m = j
    l[m],l[i] = l[i],l[m]

print(f"Sorted list l: {l}")
