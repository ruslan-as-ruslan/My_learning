n = int(input())       
m = int(input())
matrix = [list(map(int, input().split())) for i in range(n)]

maximum = int(matrix[0][0])
string = 0
column = 0

for i in range(len(matrix)):

    for j in range(len(matrix[i])):

        if maximum < int(matrix[i][j]):

            maximum = int(matrix[i][j])
            string = i
            column = j

print(string,column)

#======
'''

n, m = int(input()), int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
row, col = 0, 0
    
for i in range(n):
    for j in range(m):
        if matrix[i][j] > matrix[row][col]:
            row,col = i, j
            
print(row, col)

'''


