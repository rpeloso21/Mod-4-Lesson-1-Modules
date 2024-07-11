

def reverse_string(s):
    lst = []
    for letter in s:
        lst.append(letter)
    lst.reverse()
    new_string = "".join(lst)
    return new_string

def capitalize_string(s):
    return s.upper()

def lowercase_string(s):
    return s.lower()

def count_string(s):
    return len(s)
