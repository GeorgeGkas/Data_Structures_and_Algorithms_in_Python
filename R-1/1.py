def is_multiple(n, m):
	return n % m == 0

n = int(input("Enter integer n: "))
m = int(input("Enter integer m: "))

if is_multiple(n, m):
	print('True')
else:
	print('False')
