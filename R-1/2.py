def is_even(k):
	return k & 1

k = int(input("Enter a number: "))

if is_even(k):
	print("True")
else:
	print("False")
