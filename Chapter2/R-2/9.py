def __sub__(self, other):
    if len(self) != len(other):
        raise ValueError('dimensions must agree')

    result = Vector(len(self))
    for j in range(len(self)):
        result[j] = self[j] - other[j]

    return result
