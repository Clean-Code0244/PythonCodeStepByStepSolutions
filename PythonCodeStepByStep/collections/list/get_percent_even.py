def get_percent_even(liste):#do not modify the list
    if len(liste) == 0:
        return 0.0
    even_count = 0
    for i in liste:
        if i % 2 == 0:
            even_count += 1
    
    percentage = even_count / len(liste)

    return 100 * percentage








