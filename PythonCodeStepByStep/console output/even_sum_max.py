def even_sum():
    how_many = int(input("how many integers? "))
    even_sum = 0
    even_max = 0
    for i in range(how_many):
        a = int(input("next integer? "))
        if(a % 2 == 0):
            even_sum += a
            if(a >= even_max):
                even_max = a
    print("even sum =",even_sum)
    print("even max =",even_max)