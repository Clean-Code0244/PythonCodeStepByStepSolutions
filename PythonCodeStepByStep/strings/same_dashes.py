def same_dashes(str1, str2):
    if str1.count('-') != str2.count('-'):
        return False
    for i in range(min(len(str1), len(str2))):
        if str1[i] == '-' or str2[i] == '-':
            if (str1[i] != str2[i]):
                return False
    return True








