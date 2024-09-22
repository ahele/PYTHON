def deleteEven(listHead):
    # Write your code here
    list=[]
    for i in range(listHead):
        if i == 0:
            continue
        if i == 1:
            list.append(i)
        i = list[i-1]+listHead
        list.append(i)
    for x in list:
        if x % 2 == 0:
            list.remove(x)
    print(list)
deleteEven(3)