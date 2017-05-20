def minmax_recursive(S, n):
    """Find the minimum and maximum value from a sequence."""
    if n == 1:
        return (S[n-1], S[n-1])
    else:
        prev_minmax = minmax_recursive(S, n-1)
        max = S[n-1] if S[n-1] > prev_minmax[1] else prev_minmax[1]
        min = S[n-1] if S[n-1] < prev_minmax[0] else prev_minmax[0]
        return (min, max)

if __name__ == '__main__':
    print(minmax_recursive([0, 2, 3, -5, 484, -95965, 500], 7))
