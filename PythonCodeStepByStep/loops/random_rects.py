def random_rects():
    a = int(input("How many rectangles? "))
    total_area = 0
    for i in range(a):
        b = int(input("Width "+str(i+1)+"? "))
        c = int(input("Height "+str(i+1)+"? "))
        total_area += b*c
        for j in range(c):
            print("*"*b)
    print("Total area:",total_area)








