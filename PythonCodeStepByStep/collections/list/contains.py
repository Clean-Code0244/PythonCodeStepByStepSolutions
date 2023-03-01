def contains(list1,list2):
    if len(list1) >= len(list2):
        first = list1
        second = list2
    else:
        first = list2
        second = list1

    for i in range(len(first)):
        if first[i] == second[0]:
            a = i
            flag = True
            for j in range(len(second)):
                if second[j] != first[a]:
                    flag = False
                a += 1
            if flag:
                return True
    return False







