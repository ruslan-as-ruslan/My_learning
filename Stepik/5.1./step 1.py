lst = list(input().split())
n = int(input())

arr = []

for i in range(n):
    arr.append([])

for i in range(n):

    for j in range(i, len(lst), n):

        arr[i].append(lst[j])

print(arr)