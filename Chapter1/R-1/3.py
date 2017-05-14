def minmax(data):
	min = max = data[0]
	for number in data:
		if number < min:
			min = number
		elif number > max:
			max = number
	return (min, max)
