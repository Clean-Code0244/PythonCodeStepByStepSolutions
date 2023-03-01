def find_range_2d(liste):
    if len(liste) == 0:
        return 0
    max = liste[0][0]
    min = max
    
    for i in range(len(liste)):
        for j in range(len(liste[i])):
            if max <= liste[i][j]:
                max = liste[i][j]
            if min >= liste[i][j]:
                min = liste[i][j]
    return max-min+1








