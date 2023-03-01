def flip_half(liste):
    odd_list = []
    even_list = []
    for i in range(len(liste)):
        if i % 2==0:
            even_list.append(liste[i])
        else:
            odd_list.append(liste[i])

    reverse = []
    for i in range(len(even_list)-1,-1,-1):
        reverse.append(even_list[i])
    for i in range(len(liste)):
        if i % 2 == 0:
            liste[i] = reverse.pop()
        else:
            liste[i] = odd_list.pop()
    return liste








