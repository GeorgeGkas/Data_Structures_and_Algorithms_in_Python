def __mul__(self, other):
    if not isinstance(number, (int, float)):
        raise ValueError('other should be numerical.')

    result = Vector(len(self))

    for i in range(len(self)):
        result[i] = self[i] * other

    return result


def __rmul__(self, other):
    if other == 1:
        return self
    else:
        return self.__mul__(other)
