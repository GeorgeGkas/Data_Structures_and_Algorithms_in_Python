'''
list_reverse(data):
    left = 1
    right = data.length

    while right - left > 0:
        tmp = data[left]
        data[left] = data[right]
        data[right] = tmp
        right -= 1
        left += 1
'''

def list_reverse(data):
    left = 0
    right = len(data) - 1

    while right - left > 0:
        data[left], data[right] = data[right], data[left]
        right -= 1
        left += 1
