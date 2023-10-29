n = int(input())
mtr1 = [input().split() for i in range(n)]
m = int(input())

def holopeno(mtr1, mtr2):

    n = len(mtr1)
    k = len(mtr2)
    m = len(mtr2[0])

    result = [[0] * n for i in range(k)]
    sum = 0

    for i in range(n):    
        for j in range(k):
            sum = 0        
            for g in range(m):            
                sum += int(mtr1[i][g]) * int(mtr2[g][j])        
            result[i][j] = sum

    return result

mtr2 = mtr1

for _ in range(m-1):
    mtr2 = holopeno(mtr2, mtr1)

for r in mtr2:
    for o in r:
        print(o, end=' ')
    print() 