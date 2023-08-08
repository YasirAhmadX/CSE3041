#8th August (Problem 2 count  ) 22MIA1064 Yasir Ahmad

N = int(input("Enter no. of values: "))
l = []

for i in range(N):
    l.append(int(input("Enter value: ")))
    
countP = countN = 0

for i in l:
    if i>0:
        countP += 1
    elif i<0:
        countN += 1
    else:
        continue

print("No. of zeroes:",l.count(0))
print("No. of positives:",countP)
print("No. of negatives:",countN)
