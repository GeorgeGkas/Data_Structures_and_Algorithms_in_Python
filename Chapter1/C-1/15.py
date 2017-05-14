def unique_elems(data):
    found_numbers = {}
    for number in data:
        if number not in found_numbers:
            found_numbers[number] = number
        else:
            return False

    return True
