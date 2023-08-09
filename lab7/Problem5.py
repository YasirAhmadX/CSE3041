#9th August (Problem 5 tic tac toe) 22MIA1064 Yasir Ahmad

board = [[int(input("Enter value of box {0},{1}: ".format(i+1,j+1))) for j in range(3)]for i in range(3)]

winner = 0 #states = 0,1,2
#check rows
for i in range(3):
    if board[i][0]==board[i][1]==board[i][2]:
        winner = board[i][0]
            
#check columns
for i in range(3):
    if board[0][i]==board[1][i]==board[2][i]:
        winner = board[1][i]
        
#check diagonals
if (board[0][0]==board[1][1]==board[2][2]) or (board[2][0]==board[1][1]==board[0][2]):
    winner = board[1][1]

print("Board",*board,sep="\n")

print("Winner: ",winner)
