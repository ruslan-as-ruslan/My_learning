list_nums = input().split()


def comp(item):
    num = item
    return (sum(int(i) for i in item), int(num))


list_nums.sort(key=comp)


for item in list_nums:
    print(item, end=' ')