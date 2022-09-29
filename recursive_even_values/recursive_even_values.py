def recursive_even_values(values, low, high):
    if low >= high:
        return
    if values[low] % 2 == 0:
        print(values[low], end=' ')
    recursive_even_values(values, low + 1, high)


def print_even_values(values):
    recursive_even_values(values, 0, len(values))
