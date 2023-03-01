def contains_twice(s,c):
    count = 0
    for i in s:
        if(c == i):
            count += 1
    if(count >= 2):
        return True
    return False








