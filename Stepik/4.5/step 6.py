matrix = [input().split() for i in range(int(input()))]
length = len(matrix)

for i in range(int(length/2)):
    matrix[i], matrix[length-i-1] = matrix[length-i-1], matrix[i]

for i in matrix:
    for j in i:
        print(j, end=' ')
    print()    

