def flip_lines(text):
    lines = open(text).read().split("\n")
    for i in range(0,len(lines)-1,2):
        if i == len(lines)-2:
            lines[i] = lines[i].upper()
            continue
        lines[i],lines[i+1] = lines[i+1],lines[i]
        if i % 2 == 0:
            lines[i] = lines[i].upper()
            lines[i+1] = lines[i+1].lower()
    for i in range(0,len(lines)):
        print(lines[i])







