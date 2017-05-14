import random
def my_choice(data):
    try:
        data[0]
    except IndexError:
        print('data must be non-empty sequence.')
        exit(1)

    return data[random.randrange(0, len(data))]
