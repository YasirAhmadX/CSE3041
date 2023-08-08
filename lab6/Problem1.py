#8th August (Problem 1 list,avg ) 22MIA1064 Yasir Ahmad

N = int(input("Enter no. of students: "))
l = []

for i in range(N):
    l.append(int(input("Enter marks: ")))

print("Average marks: ",sum(l)/N)

