matrix = [input().split() for i in range(int(input()))]
el = len(matrix)

for i in range(el):
    
    matrix[i][i], matrix[el-i-1][i] = matrix[el-i-1][i], matrix[i][i]

for i in matrix:
    for j in i:
        print(j, end=' ')
    print()      