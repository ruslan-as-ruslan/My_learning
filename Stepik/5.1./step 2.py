n = int(input())
board = [input().split() for i in range(n)]
sum = []

for i in range(n):
    for j in range(n):
        if i <= j and i >= n-1-j or i >j and i >= j and i >= n-1-j:
            sum.append(board[i][j])

print(max(sum))

