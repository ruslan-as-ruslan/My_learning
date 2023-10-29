matrix = [list(map(int, input().split())) for i in range(int(input()))]
num = 0

for i in range(len(matrix)):

    for j in range(i):

        if int(matrix[i][j]) > num:
            num = matrix[i][j]

print(num)


