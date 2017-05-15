def formula(a, b, c):
    if a + b == c:
        print('{0} + {1} = {2} is True'.format(a, b , c))
    else:
        print('{0} + {1} = {2} is False'.format(a, b , c))
    
    if b - c == a:
        print('{0} - {1} = {2} is True'.format(a, b, c))
    else:
        print('{0} - {1} = {2} is False'.format(a, b, c))
        
    if a*b == c:
        print('{0} * {1} = {2} is True'.format(a, b, c))
    else:
        print('{0} * {1} = {2} is False'.format(a, b, c))
       


a = int(input('Give a: '))
b = int(input('Give b: '))
c = int(input('Give c: '))

formula(a, b, c)
