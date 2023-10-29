n,m = map(int, input().split())
mtx1 = [input().split() for i in range(n)]

print(input())

m, k = map(int, input().split())
mtx2 = [input().split() for j in range(m)]

result = [[0] * n for i in range(k)]
sum = 0

for i in range(n):    
    for j in range(k):
        sum = 0        
        for g in range(m):            
            sum += int(mtx1[i][g]) * int(mtx2[g][j])        
        result[i][j] = sum

for el in result:
    for e in el:
        print(e, end=' ')
    print()
        

