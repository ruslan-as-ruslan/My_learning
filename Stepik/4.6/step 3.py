n, m = [int(i) for i in input().split()]
num = 0
board = [[el for el in range(m)] for i in range(n)]
ls = []
fl = 0

for i in range(n):
    for j in range(m):
        fl += 1
        board[i][j] = fl
        print(str(fl).ljust(3), end ='')
    print()




