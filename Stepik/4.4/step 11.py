matrix = [list(map(int, input().split())) for i in range(int(input().split()))]

digit = 0
average = 0

for i in matrix:
    
    average = sum(i)/len(i)
    total = 0
    
    for j in i:        
        if j > average:            
            total += 1
    print(total)  