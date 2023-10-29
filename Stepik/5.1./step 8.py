n = int(input())

matrix = [[i for i in range(n)] for j in range(n)]

for i in range(1, n):
    matrix[i] = matrix[0][i::-1] + matrix[i-1][i:n-1]
    
for el in matrix:
    print(*el)