n = int(input())


matrix = [input().split() for _ in range(n)]

sum = 0

for i in range(n):
    sum += int(matrix[i][i])
print(sum)   
