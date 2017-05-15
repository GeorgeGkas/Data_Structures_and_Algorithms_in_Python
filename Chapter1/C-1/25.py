import string
def remove_punctuation(s):
    s_new = []
    for letter in s:
        if letter not in string.punctuation:
            s_new.append(letter)

    return ''.join(s_new)
