def collapse_pairs(liste):
    for i in range(0,len(liste)-1,2):
        a = liste[i]+liste[i+1]
        if a % 2 == 0:
            liste[i] = a
            liste[i+1] = 0
        else:
            liste[i + 1] = a
            liste[i] = 0
    return liste








