def all_less(a,b):
    if(not len(a)==len(b)):
        return False
    for i in range(len(a)):
        if(a[i] >= b[i]):
            return False
    return True









