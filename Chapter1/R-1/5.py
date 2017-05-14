def summation(n):
    if not isinstance(n, int):
        raise TypeError('n must be integer.')
    elif n <= 0:
        raise ValueError('n must be positive.')

    return sum([x**2 for x in range(n)])
