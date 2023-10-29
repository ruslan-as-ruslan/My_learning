n = int(input())

matrix = [['.'] * n for i in range(n)]
median = int(n/2)

for i in range(n):
    for j in range(n):
        if i == j or i == median or j == median or j == n-i-1:
            matrix[i][j] = '*'


for el in matrix:
    print(*el)



