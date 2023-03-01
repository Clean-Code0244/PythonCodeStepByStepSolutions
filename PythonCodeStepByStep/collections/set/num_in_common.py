def num_in_common(list1,list2):
    set1 = set()
    set2 = set()
    for i in list1:
        set1.add(i)
    for i in list2:
        set2.add(i)
    set3 = set1 & set2
    return len(set3)








