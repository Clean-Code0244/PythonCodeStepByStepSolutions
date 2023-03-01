def count_duplicates(liste):
    list = liste.copy()
    sum = 0
    total = 0
    for i in list:
        while list.count(i) > 1:
            list.remove(i)
            total += 1
    return total








