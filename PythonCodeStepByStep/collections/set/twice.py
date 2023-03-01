def twice(list):
    my_set = set(list)
    dictionary = {}
    for i in my_set:
        dictionary[i] = 0

    for i in list:
        if i in my_set:
            dictionary[i] += 1
    new_set = set()
    for i in dictionary.keys():
        if dictionary[i] == 2:
            new_set.add(i)
    return new_set








