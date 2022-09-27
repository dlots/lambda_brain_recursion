def recursive_palindrome(string):
    if len(string) <= 1:
        return True
    return string[0] == string[-1] and recursive_palindrome(string[1:len(string) - 1])
