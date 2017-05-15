import random

# Create a list with random size and values.
a = [random.randint(0, 100) for i in range(random.randint(0, 100))]

try:
    a[random.randint(0, 100)] += 1
except IndexError:
    print("Don’t try buffer overflow attacks in Python!")
    exit(-1)
