n = int(input())

matrix = [input().split() for i in range(n)]
matrix2 = []

for i in range(1, n**2+1):
    matrix2.append(i)

check = 'YES'

if '0' in matrix:
    check = 'NO'

for i in matrix:
    for j in i:
        if int(j) in matrix2:
            matrix2.remove(int(j))
        else:
            check = 'NO'
            break
sum = 0
for i in matrix:
    for j in i:
        sum += int(j)

sum_local = 0

for i in range(n):
    sum_local = 0
    for j in range(n):
        sum_local += int(matrix[i][j]) + int(matrix[j][i])
    if sum_local/2 != sum / n:
        check = 'NO'
        break

print(check)