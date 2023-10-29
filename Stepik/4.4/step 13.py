matrix = [list(map(int, input().split())) for i in range(int(input()))]
n = len(matrix)
num = matrix[0][0]

for i in range(n):

    for j in range(n):

        if i >= j and i <= n-1-j or i <= j and i >= n-1-j:

            if matrix[i][j] > num:

                num = matrix[i][j]

print(num)

        
