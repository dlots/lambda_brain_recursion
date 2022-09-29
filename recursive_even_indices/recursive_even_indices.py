def recursive_even_indices(values, low, high):
    while high - low > 1:
        middle = low + int((high - low) / 2)
        recursive_even_indices(values, low, middle)
        low = middle
    if low % 2 == 0:
        print(values[low], end=' ')


def even_indices(values):
    recursive_even_indices(values, 0, len(values))
