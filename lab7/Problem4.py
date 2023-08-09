#9th August (Problem 4 matix addition) 22MIA1064 Yasir Ahmad

M = int(input("Enter M: "))
N = int(input("Enter N: "))

A = [[int(input("Enter A element {0},{1}: ".format(i+1,j+1))) for j in range(N)]for i in range(M)]
B = [[int(input("Enter B element {0},{1}: ".format(i+1,j+1))) for j in range(N)]for i in range(M)]

C = [[0 for i in range(M)]for j in range(N)]

for i in range(M):
    for j in range(N):
        C[i][j] = A[i][j] + B[i][j]

print("A")
print(*A,sep="\n")
print("B")
print(*B,sep="\n")
print("C = A+B")
print(*C,sep="\n")
