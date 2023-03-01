def stutter(liste):
    for i in range(0,len(liste)+len(liste)-1,2):
        liste.insert(i,liste[i])
    return liste






