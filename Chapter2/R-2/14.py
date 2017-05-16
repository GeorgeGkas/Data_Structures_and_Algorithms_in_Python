def __mul__(self, other):
    if not isinstance(other, Vector):
        raise ValueError('two objects must be instances of Vector class.')

    result = Vector(len(self))
    for i in range(len(self)):
        result[i] = self[i] * other[i]

    return result
