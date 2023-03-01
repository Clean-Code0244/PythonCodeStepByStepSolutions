def split_stack(liste):
    first = len(liste)

    for i in range(len(liste) - 1, -1, -1):
        if (liste[i] < 0):
            liste.append(liste[i])

    for i in range(len(liste) - 1, -1, -1):
        if (liste[i] >= 0):
            liste.append(liste[i])

    for k in range(first):
        liste.pop(0)
    print(liste)







