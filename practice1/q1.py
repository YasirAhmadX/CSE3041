#23rd August (CSE3041 – Programming for Data Science Practice Questions)
#Yasir Ahmad 22MIA1064
#Q1

seq = input()
op = {"A":0,"C":0,"T":0,"G":0}

for i in seq:
    if i in op.keys():
        op[i] += 1

print(op)
