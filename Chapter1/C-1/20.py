import random
def my_shuffle(data):
    for i in range(len(data)):
        shuffled_pos = random.randint(i, len(data)-1)
        data[i], data[shuffled_pos] = data[shuffled_pos], data[i]
