l = []
stop = False
pos = 0
steps = 0

with open('day5_input.txt', 'r') as input_file:
	for line in input_file:
		l.append(int(line.rstrip('\n')))

while not stop:
	try:
		l[pos] += 1
		pos += l[pos] - 1
		steps += 1

	except IndexError:
		print(steps)
		break