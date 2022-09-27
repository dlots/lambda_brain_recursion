def recursive_digits_sum(number):
    if number == 0:
        return 0
    return recursive_digits_sum(int(number / 10)) + number % 10
