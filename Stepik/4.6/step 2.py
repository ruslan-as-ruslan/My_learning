n = int(input())

board = [[0] * n for _ in range(n)]

for i in range(n):
    board[i][n-i-1] = 1
    for j in range(n):
       if j > n-i-1:
           board[i][j] = 2


for i in board:
    for j in i:
        print(j, end=' ')
    print()

