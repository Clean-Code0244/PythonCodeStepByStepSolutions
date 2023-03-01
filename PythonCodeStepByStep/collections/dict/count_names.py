dict = {}
while True:
    str = input("Enter name: ")
    if len(str) == 0:
        for (k,v) in dict.items():
            print("Entry ["+k+"] has count",v)
        break
    else:
        if not str in dict:
            dict[str] = 1
        else:
            dict[str] += 1








