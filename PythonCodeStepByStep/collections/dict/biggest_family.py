def biggest_family(str):
    file = open(str).read().split()
    dictionary = {}
    name = []
    surname = []

    for i in range(0,len(file),2):
        name.append(file[i])
        surname.append(file[i+1])

    for i in range(len(surname)):

        if not surname[i] in dictionary.keys() :
            dictionary[surname[i]] = 1
        else:
            dictionary[surname[i]] += 1

    a = find_Max(dictionary)
    most_frequent = []
    for i in dictionary.keys():
        if dictionary[i] == a:
            most_frequent.append(i)
    final_name = []
    for i in most_frequent:
        empty = []
        for j in range(len(surname)):
            if surname[j] == i:
                empty.append(name[j])
        final_name.append(empty)
    dictionary1 = {}
    for i in range(len(most_frequent)):
        dictionary1[most_frequent[i]] = ""
        for j in range(len(final_name[i])):
            dictionary1[most_frequent[i]] += final_name[i][j]+" "
    result = sorted(dictionary1.items(),key=lambda x:x[0])
    kisi = []
    for i in range(len(result)):
        kisi.append(result[i][0])

    new_sort = []
    for k in result:
        a = 0
        empty = []
        for j in range(len(k[1])):
            if k[1][j] == " ":
                empty.append(k[1][a:j])
                a = j + 1
        new_sort.append(empty)
    off = []
    for i in range(len(new_sort)):
        yeterda = sorted(new_sort[i],key=lambda x:x[:])
        off.append(yeterda)
    for i in range(len(kisi)):
        print(kisi[i]+" family: ",end="")
        for j in range(len(off[i])):
            print(off[i][j]+" ",end="")
        print()


def find_Max(dictionary):
    max = 0
    for i in dictionary.values():
        if max <= i:
            max = i
    return max
#I think this solution is not a very efficent solution :)

