def minmax(data):
	min = max = data[0]
	for number in data:
		if number < min:
			min = number
		elif number > max:
			max = number
	return (min, max)

user_input = input("Enter the numbers to check (seperated by ,): ")
data = [int(x, 10) for x in user_input.split(",")]

min, max = minmax(data)
print ("Min:", min, "Max:", max)
