def matrix_add(list1,list2):
    first = []
    
    for i in range(len(list1)):
        temp_list = []
        for j in range(len(list1[i])):
            temp_list.append(list1[i][j] + list2[i][j])
        first.append(temp_list)
    return first








