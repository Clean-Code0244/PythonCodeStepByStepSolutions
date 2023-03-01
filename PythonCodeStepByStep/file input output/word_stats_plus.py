def word_stats_plus(files):
    file = open(files).read().split("\n")
    new_array = []

    for i in file:
        new_array.append(i.lower())
    total_line = len(new_array)
    if new_array[len(new_array) - 1] == "":
        total_line -= 1

    words = []
    for i in new_array:
        words.append(i.split())

    number_of_words = 0
    for i in range(len(words)):
        number_of_words += len(words[i])

    char = [" ", ",", ".", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    new_file = []
    new_set = set()
    for i in new_array:
        for j in range(len(i)):
            if ord(i[j]) >= ord("a") and ord(i[j]) <= ord("z"):
                new_set.add(i[j])
    new_word = []
    for i in new_array:
        for j in range(len(i)):
            # if ord(i[j])>=ord("a") and ord(i[j])<=ord("z"):
            if i[j] != " ":
                new_word.append(i[j])

    length = len(new_word)

    unique = len(new_set)

    my_set = set()
    for i in new_file:
        my_set.add(i)
    average = int(unique / 26 * 100)

    print("Total lines =", total_line)
    print("Total words =", number_of_words)



    print(str("Total unique letters = " + str(unique) + " (" + str(average) + "% of alphabet)"))


    print("Average words/line =", round(number_of_words / total_line, 1))
    print("Average word length =", round(length / number_of_words, 1))

