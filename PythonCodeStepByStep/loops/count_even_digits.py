def count_even_digits(first,second):
    count = 0
    for i in range(second):
        if(first % 2== 0):
            count += 1
        first //= 10
    return count
        








