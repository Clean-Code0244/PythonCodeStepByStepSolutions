def intersect(dict1,dict2):
    dict3 = {}
    for (k,l) in dict1.items():
        for (m,n) in dict2.items():
            if k==m and l == n:
                dict3[k] = l
    return dict3








