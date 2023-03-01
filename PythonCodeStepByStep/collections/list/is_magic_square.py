def is_magic_square(liste):
    a = len(liste)
    count = 0
    for i in range(len(liste)):
        for j in range(len(liste[i])):
            count += 1
    if a**2 != count :
        return False
    if a == 0:
        return True


    newlist = []

    for i in range(len(liste)):
        sum = 0
        for j in range(len(liste[i])):
            sum += liste[i][j]
        newlist.append(sum)
    temp = newlist[0]
    for i in newlist:
        if i != temp:
            return False
    return True


