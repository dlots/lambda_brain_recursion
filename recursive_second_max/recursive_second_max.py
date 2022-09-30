def recursive_second_max(values, low, high, max_value, second_max_value):
    if low >= high:
        return max_value, second_max_value
    value = values[low]
    if max_value is None:
        max_value = value
    elif max_value < value:
        max_value, second_max_value = value, max_value
    elif value < max_value and (second_max_value is None or second_max_value < value):
        second_max_value = value
    return recursive_second_max(values, low + 1, high, max_value, second_max_value)


def second_max(values):
    result = recursive_second_max(values, 0, len(values), None, None)
    (_, second_max_value) = result
    return second_max_value
