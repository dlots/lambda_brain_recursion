def recursive_even_values(values, low, high):
    while high - low > 1:
        middle = low + int((high - low) / 2)
        recursive_even_values(values, low, middle)
        low = middle
    if values[low] % 2 == 0:
        print(values[low], end=' ')


def print_even_values(values):
    recursive_even_values(values, 0, len(values))