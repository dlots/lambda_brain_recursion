def recursive_even_values(values):
    if len(values) > 1:
        middle_index = int(len(values) / 2)
        recursive_even_values(values[:middle_index])
        recursive_even_values(values[middle_index:])
    elif values[0] % 2 == 0:
        print(values[0], end=' ')

