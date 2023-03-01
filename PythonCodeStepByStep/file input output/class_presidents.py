def class_presidents(filename):
    file = open(filename)
    read = file.read()
    all_students = read.split()
    president= []
    junior = []
    for i in range(1,len(all_students),3):
        part = []
        if all_students[i]=="s":
            part.append(all_students[i-1])
            part.append(all_students[i + 1])
            president.append(part)
        else:
            part.append(all_students[i - 1])
            part.append(all_students[i + 1])
            junior.append(part)
    a = findMax(president)
    winner_president = president[a][0]
    winner_president_vote = president[a][1]

    b = findMax(junior)
    winner_junior = junior[b][0]
    winner_junior_vote = junior[b][1]

    print("Sophomore Class President:",winner_president,"("+str(winner_president_vote)+" votes)")
    print("Junior Class President:",winner_junior,"("+str(winner_junior_vote)+" votes)")

def findMax(liste):
    max = liste[0][1]
    max_index = 0
    for i in range(len(liste)):

        if max <= liste[i][1]:
            max = liste[i][1]
            max_index = i
    return max_index








