ls = input().split()
n = int(ls[0])
m = int(ls[1])

matrix = []
arr = []
flag = -1

for i in range(n):
    arr = []
    flag += 1
    for j in range(m):    
        if flag % 2 == 0:
            arr.append('.')
            flag += 1
        else:
            arr.append('*')
            flag += 1
    if j == 0:
        flag += 1
    matrix.append(arr)
    
for i in matrix:
    for j in i:
        print(j, end=' ')
    print()



'''

n, m = [int(i) for i in input().split()]
board = [['.'] * m for _ in range(n)]

for i in range(n):
    for j in range(1 - i % 2, m, 2):
        board[i][j] = '*'

for row in board:
    print(*row)

'''


