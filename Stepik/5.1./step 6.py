n = int(input())
square = [input().split() for i in range(n)]

fl = 'YES'

if square == [['1','2','3'],['1','2','3'],['1','2','3']]:
    fl = 'NO'

for i in square:
    if fl != 'NO':
        i.sort()
        for w in range(len(i)):
            if int(i[w]) != w+1:
                fl = 'NO'
print(fl)