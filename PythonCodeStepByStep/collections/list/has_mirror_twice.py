def has_mirror_twice(a1,a2):
    count = 0
    temp_array = []
    reverse_array = []
    for i in a2:
        temp_array.append(i)
    for  i in range(len(temp_array)//2):
        temp_array[i],temp_array[len(temp_array)-1-i] = temp_array[len(temp_array)-1-i],temp_array[i]
    for i in temp_array:
        reverse_array.append(i)
    if len(a1) >= len(reverse_array):
        first = a1
        second = reverse_array
    else:
        first = reverse_array
        second = a1
    for i in range(len(first)):
        if first[i] == second[0]:
            a = i
            flag = True
            for j in range(len(second)):
                if second[j] != first[a]:
                    flag = False
                a += 1
                if a >= len(first) and flag == False:
                    return False
            if flag:
                count += 1
            if flag and count >= 2:
                return True
    return False






