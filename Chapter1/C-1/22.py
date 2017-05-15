a = [int(x, 10) for x in input('Give first sequence of numbers (seperated by ,): ').split(',')]
b = [int(x, 10) for x in input('Give second sequence of numbers (seperated by ,): ').split(',')]

c = []
for i in range(len(a)):
    c.append(a[i]*b[i])
