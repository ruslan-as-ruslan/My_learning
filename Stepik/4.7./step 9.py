n,m = map(int, input().split())

mtr1 = [input().split() for i in range(n)]
print(input())
mtr2 = [input().split() for j in range(n)]

res = []
el = 0

for i in range(n):
    res.append([])
    for j in range(m):
        el = int(mtr1[i][j])+int(mtr2[i][j])        
        res[i].append(el)

for i in res:
    print(*i)

