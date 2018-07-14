import time
with open('day9_input.txt', 'r') as file: # read input
	input_text = file.readline()

class Tree():
	def __init__(self, group):
		self.group = group
		self.level = 0
		self.points = 0
		self.pointer = 0
		self.get_points()

	def get_points(self):
		while True:
			#time.sleep(0.0001/(10000**50))

			try:
				if self.group[self.pointer] == '{':
					self.level += 1
					#print(' '*self.level + f'going down to level {self.level}')
					self.points += self.level

				elif self.group[self.pointer] == '}':
					self.level -= 1
					#print(' '*self.level + f'going up to level {self.level}')
				self.pointer += 1
			except IndexError:
				break

class Stream():

	def __init__(self, input_text):
		self.input_text = input_text
		self.input_list = list(input_text)
		self.pointer = 0
		self.score = 0
		self.garbage_count = 0
		self.level = 0
		self.remove_garbage()
		self.get_score()
		self.printer()

	def remove_garbage(self):
		while True:
			if self.input_text.find('<') == -1:
				break
			garbage = self.find_garbage(self.input_text.find('<'))
			#print(f'garbage between {garbage}')
			self.input_list[garbage[0]:garbage[1]] = ''
			self.garbage_count += (garbage[1] - garbage[0]) - 2 
			self.input_text = ''.join(self.input_list)

		#print(f'input_text is now {self.input_text}')

	def find_garbage(self, index):
		self.input_list[index]
		end = index
		while True:
			end += 1
			try:
				if self.input_list[end] == '!':
					self.garbage_count -= 2
					end += 1

				elif self.input_list[end] == '>':
					break
				
				else:
					pass
			except IndexError:
				print('List done!')
				break

		return index, end + 1

	def get_levels(self, group):
		self.score += 1
		self.level = 1

		while True:
			index = group.find('{')
			#group[index] = ''
			self.score += self.level
			break

	def get_score(self):
		output_list = ''.join(self.input_text.split(','))
		#print(output_list)
		#for group in output_list:
		#	self.get_levels(group)
		self.score = Tree(output_list).points

	def printer(self):
		print(f'Score {self.score}\nFound {self.garbage_count} garbage caracters')


program = Stream(input_text)
#print(program.input_text[5:program.find_garbage(5)])
#nu är programmet exakt 100 rader
#print (program.input_text)