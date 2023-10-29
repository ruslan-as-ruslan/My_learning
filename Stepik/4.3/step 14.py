lst = input().split()

sub_lst = [[]]

for i in range(len(lst)):   
    for j in range(len(lst)-i):
        sub_lst.append(lst[j:j+i+1])
print(sub_lst)




    

         
