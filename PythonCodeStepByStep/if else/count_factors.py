def count_factors(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:   # a factor 
            count += 1
    return count