lenght = 8
chess_desk = [['.' for i in range(lenght)] for j in range(lenght)]

place = input()

line = '87654321'.index(place[1])
column = 'abcdefgh'.index(place[0])

chess_desk[line][column] = 'N'

item = 0

for i in range(len(chess_desk)):
    for j in range(len(chess_desk[i])):  
        item = (line-i) * (column-j)        
        if item == 2 or item == -2:            
            chess_desk[i][j] = '*'
            
for i in chess_desk:
    for j in i:
        print(j, end=' ')
    print() 







