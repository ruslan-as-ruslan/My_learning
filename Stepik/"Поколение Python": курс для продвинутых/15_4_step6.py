list_nums = input().split()

def comparator(item):
    return sum(int(i) for i in item)

list_nums.sort(key=comparator)

for item in list_nums:
    print(item, end=' ')