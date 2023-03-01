def swap_pairs(liste):
    for i in range(0,len(liste)-1,2):
        liste[i],liste[i+1] = liste[i+1],liste[i]
    return liste








