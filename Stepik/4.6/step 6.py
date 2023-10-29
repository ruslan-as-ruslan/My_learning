n = int(input())
matrix = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    for j in range(n):
        if i <= n/2 and i <= j and i <= n-1-j:
            matrix[i][j] = 1
        elif i >= n/2 and i >= j and i >= n-1-j:
            matrix[i][j] = 1

for i in matrix:
    for j in i:
        print(str(j).ljust(3), end= ' ')
    print()
       