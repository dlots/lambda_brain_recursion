def recursive_palindrome(string):
    if len(string) <= 1:
        return True
    if string[0] != string[-1]:
        return False
    return recursive_palindrome(string[1:len(string) - 1])
