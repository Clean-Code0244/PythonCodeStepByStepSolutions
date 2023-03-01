def scale_by_k(liste):
    
    a= 0
    b = len(liste)
    c = b
    while a < b:
        deger = liste[a]
        for i in range(deger):
            liste.append(deger)
        a += 1
    for i in range(c):
        liste.pop(0)
    return liste








