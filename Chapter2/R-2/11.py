"""
We also have to declare a method called __radd__. This happens because when we
type [5, 3, 10, -2, 1] + u python try to call [5, 3, 10, -2, 1].__add__(u).
But python list type doesn't know anything about how to add the Vector
instance, so it tries to call the reverse add method __radd__ which is not 
yet defined.
"""

def __radd__(self, other):
    return self.__add__(other)
