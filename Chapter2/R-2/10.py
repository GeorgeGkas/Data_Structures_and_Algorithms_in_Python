def __neg__(self):
    result = Vector(len(self))

    for i in range(len(self)):
        result[i] = self[i] * (-1)

    return result
