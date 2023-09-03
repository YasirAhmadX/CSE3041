A = []
for i in range(4):
    row = []
    for j in range(4):
        row.append(int(input("Enter element {0},{1}: ".format(i+1,j+1))))
    A.append(row)

print(*A,sep="\n")

#col sum
col_sum = []
row_prod = []
for i in range(4):
    Sum= 0
    prod = 1
    for j in range(4):
        Sum += A[j][i]
        prod *= A[i][j]
    col_sum.append(Sum)
    row_prod.append(prod)

print("Min column sum: ",min(col_sum))
print("Min column sum index: ",col_sum.index(min(col_sum)))
print("Max row product: ",max(row_prod))
print("Max row product index: ",row_prod.index(max(row_prod)))
