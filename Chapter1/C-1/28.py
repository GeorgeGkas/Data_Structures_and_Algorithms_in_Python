import math

def norm(v, p = 2):
    norm_sum = 0
    for point in v:
        norm_sum += point**p

    return norm_sum ** (1.0 / p)
