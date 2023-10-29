n = int(input())
n1, n2, n3 = 1, 1, 1
next = 0
for i in range(n):
    print(n1, end=' ')
    next = n1 + n2 + n3
    n1, n2, n3 = n2, n3, next

