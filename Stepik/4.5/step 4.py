matrix = [input().split() for i in range(int(input()))]

answer = 'YES'


for i in range(len(matrix)):
    for j in range(len(matrix[i])):
            if matrix[i][j] != matrix[j][i] and i != j:
                answer = 'NO'
                break

                               
print(answer) 



