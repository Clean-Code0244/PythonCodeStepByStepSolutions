def longest_sorted_sequence(list):
    if len(list) == 0:
        return  0
    max = 1
    count = 1
    for i in range(len(list)-1):

        if list[i] <= list[i+1]:
            count += 1
            if count >= max:
                max = count

        else:
            count = 1
    return max








