def chunked(piece: str, n: list):

    piece = piece.split()
    n = int(n[0])
    chanked_list = []
    sub_list = []

    for i in piece:

        sub_list.append(i)

        if len(sub_list) == n:
            chanked_list.append(sub_list)
            sub_list = []
    if sub_list != []:
        chanked_list.append(sub_list)
    return chanked_list

piece = str(input())
n = str(input())

print(chunked(piece, n))






        







        

















