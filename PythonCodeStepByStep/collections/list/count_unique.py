def count_unique(list):
    liste = []
    total = 0
    for i in list:
        liste.append(i)

    while len(liste) > 0:
        b = liste[0]
        a = liste.count(b)
        while a > 0:
            liste.remove(b)
            a -= 1
        total += 1
    return total








