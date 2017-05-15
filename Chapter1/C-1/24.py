def vowels_count(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    string_lowered = string.lower()

    counter = 0
    for letter in string_lowered:
        if letter in vowels:
            counter += 1

    return counter
