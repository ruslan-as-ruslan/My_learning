matrix = [input().split() for i in range(int(input()))]
length = len(matrix)
matrix2 = []

for i in range(length):
    for j in range(length):
        print(matrix[length-j-1][i], end=' ')
    print()

