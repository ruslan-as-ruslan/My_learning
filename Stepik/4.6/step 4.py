n, m = [int(i) for i in input().split()]
board = [[1 for i in range(m)] for j in range(n)]
fl = 0
for i in range(m):
    for j in range(n):
        fl += 1
        board[j][i] = i * n + j + 1

for i in board:
    for j in i:
        print(str(j).ljust(3), end= ' ')
    print()    

