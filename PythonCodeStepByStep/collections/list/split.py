import math
def split(list):
    a = 0
    b = 0
    new_list = []
    for i in range(len(list)):
        a = math.ceil(list[i] / 2)
        b = list[i] - a
        new_list.append(a)
        new_list.append(b)
    return new_list








