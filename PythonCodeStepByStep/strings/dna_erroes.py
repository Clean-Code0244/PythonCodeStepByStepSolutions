def dna_errors(dna1, dna2):
    errors = 0
    errors += abs(len(dna1) - len(dna2))
    err = 0
    for i in range(min(len(dna1),len(dna2))):
        if dna1[i] == 'A' and dna2[i] != 'T':
            err += 2
        elif dna1[i] == 'T' and dna2[i] != 'A':
            err += 2
        elif dna1[i] == 'C' and dna2[i] != 'G':
            err += 2
        elif dna1[i] == 'G' and dna2[i] != 'C':
            err += 2

    errors += err
    errors += dna1.count('-')
    errors -= dna2.count('-')
    return errors






