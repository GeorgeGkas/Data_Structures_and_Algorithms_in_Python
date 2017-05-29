def addrange(start, stop):
    i = start
    step = 0
    while i < stop:
        yield i
        step += 2
        i += step


a = [x for x in addrange(0, 91)]
print(a)
