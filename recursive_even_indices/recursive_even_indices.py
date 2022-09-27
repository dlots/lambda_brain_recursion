def recursive_even_indices(values, starts_with_even=True):
    if len(values) > 2:
        middle_index = int(len(values) / 2)
        recursive_even_indices(values[:middle_index], starts_with_even)
        recursive_even_indices(values[middle_index:], (middle_index % 2 == 0) == starts_with_even)
        return
    elif len(values) == 1 and starts_with_even:
        print(values[0], end=' ')
        return
    elif len(values) == 2 and starts_with_even:
        print(values[0], end=' ')
        return
    elif len(values) == 2 and not starts_with_even:
        print(values[1], end=' ')
        return
