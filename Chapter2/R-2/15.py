def __init(self, d):
    if isinstance(d, list):
        """Create a vector based on the list."""
        self._coords = d
    else:
        """Create d-dimensional vector of zeros."""
        self._coords = [0] * d
