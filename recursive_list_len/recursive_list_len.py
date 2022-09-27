def recursive_list_len(list_):
    if list_:
        list_.pop()
        return recursive_list_len(list_) + 1
    return 0

