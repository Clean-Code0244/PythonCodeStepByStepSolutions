def binary_to_decimal(num):
    gecici_sayi = num
    count = 0
    sum = 0
    while(gecici_sayi > 0):
        count += 1
        gecici_sayi //=10
    for i in range(count):
        sum += (num%10)*(2**i)
        num //= 10
    return sum
        








