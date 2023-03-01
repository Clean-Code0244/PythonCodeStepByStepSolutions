def find_median(liste):
    temp_list = []
    for i in liste:
        temp_list.append(i)
    newlist = []
    a = len(temp_list)
    while len(temp_list)>0:
        newlist.append(min(temp_list))
        temp_list.remove(min(temp_list))

    return newlist[a//2]








