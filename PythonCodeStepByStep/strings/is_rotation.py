def is_rotation(str1,str2):
    #find the index
    if len(str1) == 0 and len(str2) == 0:
        return True
    if len(str1) == 0 or len(str2) == 0:
        return False
    a = 0
    for i in range(len(str1)):
        if str2[0] == str1[i]:
            a = i
            break
    newstring = str1[a:]+str1[:a]
    if str2 != newstring:
        return False
    return True








