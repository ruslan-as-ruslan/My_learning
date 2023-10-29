n = int(input())
matrix = []        
for i in range(n): 
        arr = [int(num) for num in input().split()]
        matrix.append(arr)

up_quater = 0
left_quater = 0
right_quater = 0
down_quater = 0
        
for i in range(n):
        
        for j in range(n):

            if i > j and i < n-1-j:
                left_quater += matrix[i][j]
            
            elif i > j and i > n-1-j:
                down_quater += matrix[i][j]    
            
            elif i < j and i > n-1-j:
                right_quater += matrix[i][j]
            
            elif i < j and i < n-1-j:
                up_quater += matrix[i][j]                 

print('Верхняя четверть:', up_quater)
print('Правая четверть:', right_quater)
print('Нижняя четверть:', down_quater)
print('Левая четверть:', left_quater)               