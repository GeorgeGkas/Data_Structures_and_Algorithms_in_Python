def summation(n):
    if not isinstance(n, int):
        raise TypeError('n must be integer.')
    elif n <= 0:
        raise ValueError('n must be positive.')

    sum = 0
    for i in range(n):
        sum += i**2

    return sum
