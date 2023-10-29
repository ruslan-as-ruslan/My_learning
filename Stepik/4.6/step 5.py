n = int(input())
board = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    for j in range(n):
        board[j][j] = 1
        board[j][n-j-1] = 1

for i in board:
    for j in i:
        print(str(j).ljust(3), end=' ')
    print()    