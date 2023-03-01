def reverse_chunks(word,number):
    a = 0
    new_str = ""
    for i in range(number, len(word) + 1, number):
        new_str+=word[a:i][-1:-len(word[a:i])-1:-1]
        a = i
    if len(word) != len(new_str):
        new_str+= word[a:]
    elif len(word)<number:
        new_str+=word
    return new_str







