n, m = [int(i) for i in input().split()]
board = [[i+1 for i in range(m)] for j in range(n)]

for i in range(1, n):
    board[i] = board[i-1][1:m]
    board[i] += str(board[i-1][0])
        
for i in board:
    for j in i:
        print(str(j).ljust(3), end='')
    print()


'''

n, m = [int(i) for i in input().split()]
matrix = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        matrix[i][j] = (i + j) % m + 1
          
for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()


'''    