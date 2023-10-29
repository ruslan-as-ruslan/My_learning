n = int(input())

contest = [input().split() for i in range(n)]

for student in contest:
    print(' '.join(student))
print('')

for k in range(n):
    if int(contest[k][1]) > 3:
        print(' '.join(contest[k]))

