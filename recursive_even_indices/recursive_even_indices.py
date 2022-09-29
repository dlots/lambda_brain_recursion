def recursive_even_indices(values, low, high):
    if low >= high:
        return
    if low % 2 == 0:
        print(values[low], end=' ')
    recursive_even_indices(values, low + 1, high)


def print_even_indices(values):
    recursive_even_indices(values, 0, len(values))
