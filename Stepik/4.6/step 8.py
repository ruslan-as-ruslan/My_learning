n, m = [int(i) for i in input().split()]
snake = [[i for i in range(m)] for j in range(n)]

for i in range(n):
    for j in range(m):
        if i % 2 == 0:
            snake[i][j] = i*m + j + 1
        if i % 2 != 0:
            snake[i][m-1-j] = i*m + j +1

for i in snake:
    for j in i:
        print(str(j).ljust(3), end='')
    print()    