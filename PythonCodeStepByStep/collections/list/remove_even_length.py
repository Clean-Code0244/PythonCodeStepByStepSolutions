def remove_even_length(list):

    i = 0
    while i < len(list):
        if len(list[i]) % 2 == 0:
            list.remove(list[i])
        else:
            i += 1
    return  list







