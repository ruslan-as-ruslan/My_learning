n = int(input())
m = int(input())

matrix = [[input() for _ in range(m)] for _ in range(n)]

for i in range(n):

    for j in range(m):
        print(matrix[i][j], end= ' ')
    print()

print('')

for i in range(m):

    for j in range(n):
        print(matrix[j][i], end= ' ')
    print()

