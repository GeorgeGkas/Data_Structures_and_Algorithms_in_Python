def odd_summation(n):
    if not isinstance(n, int):
        raise TypeError('n must be integer.')
    elif n <= 0:
        raise ValueError('n must be positive.')

    sum = 0
    for num in range(n):
        if num % 2 == 1:
            sum += num**2

    return sum
