def __eq__(self, other):
    if len(self) != len(other):
        raise ValueError('Sequence instances should have the same size.')

    for i in range(len(self)):
        if self[i] != other[i]:
            return False

    return True
