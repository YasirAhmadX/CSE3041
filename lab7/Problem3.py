#9th August (Problem 3) 22MIA1064 Yasir Ahmad
"""
A and B have M money. In a ice cream shop they have N flavours with N costs.
A and B have to spend all the moeny.
WAP to identify 2 flavours for A and B
"""
M = int(input("Enter M: "))
N = int(input("Enter N: "))

cost = []

for i in range(N):
    cost.append(int(input("Enter cost for flavour {0}: ".format(i+1))))

for i in range(N):
    f1c = cost[i]
    
    f2c = M - f1c

    fl_avail = cost[i+1::]

    if fl_avail.count(f2c)>0:
        print(cost.index(f1c),fl_avail.index(f2c)+i+1)
    
"""
"""
