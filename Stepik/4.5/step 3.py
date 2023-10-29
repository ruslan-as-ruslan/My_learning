n, m = int(input()), int(input())

matrix = [[int(i) for i in input().split()] for _ in range(n)]

index = input().split()
i = int(index[0])
j = int(index[1])

for el in range(len(matrix)):
    matrix[el][i], matrix[el][j] = matrix[el][j], matrix[el][i]
 
    
for i in matrix:
    for j in i:
        print(j, end=' ')
    print()   

#====

'''
n, m = int(input()), int(input())
matrix = [input().split() for _ in range(n)]
col1, col2 = [int(i) for i in input().split()]

for i in range(n):
    matrix[i][col1], matrix[i][col2] = matrix[i][col2], matrix[i][col1]

for row in matrix:
    print(*row)

'''