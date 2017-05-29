def dividedtimes(x):
    if not isinstance(x, int):
        raise TypeError('x must be integer.')
    elif x <= 2:
        raise ValueError('x must be greater than 2.')

    counter = 0
    while x >= 2:
        x = x / 2
        counter += 1
    
    return counter
