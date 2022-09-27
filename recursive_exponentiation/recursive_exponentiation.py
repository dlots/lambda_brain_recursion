def recursive_exponentiation(base, power):
    if power == 0:
        return 1
    elif base == 0 or power == 1:
        return base
    return recursive_exponentiation(base, power - 1) * base
