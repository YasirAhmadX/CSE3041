#23rd August (CSE3041 – Programming for Data Science Practice Questions)
#Yasir Ahmad 22MIA1064
#Q3
l = []
for i in range(int(input("Enter N: "))):
    o =input("Enter name, age, rating: ")
    l.append(o.split())


print("List 1 (Under the age of 20)")
for i in l:
    if int(i[1])<= 20:
        print(*i,sep=" ")
print("List 2 (Above the age of 20)")    
for i in l:
    if int(i[1])> 20:
        print(*i,sep=" ")
