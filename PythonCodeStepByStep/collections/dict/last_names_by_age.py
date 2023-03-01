def last_names_by_age(dict1,minage,maxage):
    dictionary = {}
    for i in dict1.values():
        lastname = ""
        for j in dict1.keys():
            if dict1[j] == i:
                a = j.split()
                lastname += " and "+a[len(a)-1]
        if i >= minage and i <= maxage:
            dictionary[i] = lastname[5:len(lastname)]
    return dictionary








