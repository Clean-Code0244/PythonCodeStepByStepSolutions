def sorted(list):
    for i in range(len(list)-1):
        if not (list[i] < list[i+1]):
            return False
    return True








