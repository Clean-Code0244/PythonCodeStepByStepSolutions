def starters(liste,count):
    dictionary = {}
    new_list = []
    for i in range(len(liste)):
        new_list.append(liste[i][:1].lower())

    for i in new_list:
        if not i in dictionary.keys():
            dictionary[i] = 1
        else:
            dictionary[i]+=1

    my_set = set()
    for (k,v) in dictionary.items():
        if v >= count and (k != "" and k != " "):
            my_set.add(k)
    sorted_set = sorted(my_set,key=lambda x:x[0])
    original_set = set()
    for i in sorted_set:
        original_set.add(i)
    return original_set







