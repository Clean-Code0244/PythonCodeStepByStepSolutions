def rarest_age(dictionary):
    if len(dictionary) == 0:
        return 0
    
    my_set = set()
    second_dict = {}
    for i in dictionary.values():
        my_set.add(i)
    for i in my_set:
        second_dict[i] = 0
        for j in dictionary.values():
            while j == i:
                second_dict[i] += 1
                break

    counter_list = []
    age_list = []
    a = find_mins(second_dict)
    for (i,j) in second_dict.items():
        if a == j:
            counter_list.append(j)
            age_list.append(i)
    a = find_min(age_list)
    return age_list[a]


def find_mins(dict):
    list = []
    for i in dict.values():
        list.append(i)

    min = list[0]
    for i in list:
        if min >= i:
            min = i
    return min
def find_min(list):
    min = list[0]
    pos = 0
    for i in range(len(list)):
        if min > list[i]:
            min = list[i]
            pos = i
    return pos








