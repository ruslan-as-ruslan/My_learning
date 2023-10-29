n = int(input())
matrix = [input().split() for i in range(n)]
matrix2 = [[0] * n for i in range(n)]

for i in range(n):
    for j in range(n):
        matrix2[i][j] = matrix[j][i]


for i in matrix2:
    for j in i:
        print(j, end=' ')
    print()  