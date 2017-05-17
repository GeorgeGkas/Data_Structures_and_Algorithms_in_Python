class ReversedSequenceIterator:
    def __init__(self, sequence):
        self._seq = sequence
        self._k = len(sequence)

    def __next__(self):
        self._k -= 1
        if self._k > -1:
            return(self._seq[self._k])
        else:
            raise StopIteration()

    def __iter__(self):
        return self
