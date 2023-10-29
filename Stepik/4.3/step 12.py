list1 = str(input())
list1 = list1.split()

sublist = []
mainlist = []

for char in list1:

    if sublist == []:

        sublist.append(char)
    
    elif sublist != []:

        if sublist[0] == char:

            sublist.append(char)
        else:
            
            mainlist.append(sublist)
            sublist = []
            sublist.append(char)
if sublist != []:
    mainlist.append(sublist)
        
print(mainlist)  









    










    

