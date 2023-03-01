def boy_girl(text):
    file = open(text)
    read = file.read()
    all_people = read.split()
    all_class = []
    boys = []
    girls = []
    for i in range(0,len(all_people),2):
        parts = []
        parts.append(all_people[i])
        parts.append(all_people[i+1])
        all_class.append(parts)
    for i in range(len(all_class)):
        if i % 2 == 0:
            boys.append(all_class[i])
        else:
            girls.append(all_class[i])
    sum_boys = 0
    sum_girls = 0
    for i in range(0,len(boys)):
        sum_boys += int(boys[i][1])
    for i in range(0,len(girls)):
        sum_girls += int(girls[i][1])
    print(len(boys),"boys,",len(girls),"girls")
    
    print("Difference between boys' and girls' sums:",abs(sum_girls-sum_boys))








