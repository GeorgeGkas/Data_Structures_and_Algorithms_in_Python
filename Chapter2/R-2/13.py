def __rmul__(self, other)
    if other == 1:
        return self                                                            
    else:
        return self.__mul__(other)
