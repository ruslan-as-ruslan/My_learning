n, m = map(int, input().split())
lst = [[i] * m for i in range(n)]
nm = 0
for q in range(n+m-1):
    for i in range(n):
        for j in range(m):
            if i+j == q:
                nm += 1
                lst[i][j] = nm
                
for i in lst:
    for j in i:
        print(str(j).ljust(3), end='')
    print()        


'''

1 - 0, 0;                       #3 
2 - 0, 1;   1, 0;               #2
3 - 0, 2;   1, 1;     2, 0;     #1
4 - 0, 3;   1, 2;     2, 1;     #0
5 - 0, 4;   1, 3;     2, 2;     #-1
6 - 1, 4;   2, 3;               #-2
7 - 2, 4;                       #-3 

'''





