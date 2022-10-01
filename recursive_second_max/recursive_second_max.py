def recursive_second_max(values, low, high, max_value, second_max_value):
    if low >= high:
        return max_value, second_max_value
    value = values[low]
    if max_value < value:
        max_value, second_max_value = value, max_value
    elif second_max_value < value < max_value:
        second_max_value = value
    return recursive_second_max(values, low + 1, high, max_value, second_max_value)


def second_max(values):
    initial_max, initial_second_max = values[0], values[1]
    if initial_max < initial_second_max:
        initial_max, initial_second_max = initial_second_max, initial_max
    result = recursive_second_max(values, 2, len(values), initial_max, initial_second_max)
    (_, second_max_value) = result
    return second_max_value
