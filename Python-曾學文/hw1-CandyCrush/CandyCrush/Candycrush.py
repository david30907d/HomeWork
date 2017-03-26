import random, collections
class Candycrush(object):
	"""docstring for candycrush"""
	def __init__(self):
		self.length, self.width = 10, 10
		self.numOfColor = None
		self.round = 20
		self.Color = ['0;31;40', '0;32;40', '0;33;40', '0;34;40', '0;35;40', '0;36;40', '0;37;40', '0;30;41', '0;32;41', '0;33;41', '0;34;41', '0;35;41', '0;36;41', '0;37;41', '0;30;42', '0;31;42', '0;33;42', '0;34;42', '0;35;42', '0;36;42', '0;37;42', '0;30;43', '0;31;43', '0;32;43', '0;34;43', '0;35;43', '0;36;43', '0;37;43', '0;30;44', '0;31;44', '0;32;44', '0;33;44', '0;35;44', '0;36;44', '0;37;44']
		self.table = {}
		self.detectQue = []

	def getColorCandy(self):
		return '\x1b[{}m 🍬 \x1b[0m'.format(self.Color[random.randint(0, self.numOfColor-1)])

	def CollisionDetect(self):
		for position, value in self.table.items():
			if self.Collision_patrol(position, 'right')==False:self.CollisionDetect()
			if self.Collision_patrol(position, 'down')==False:self.CollisionDetect()

	def Collision_patrol(self, position, direction):
		if direction == 'right':
			if position%10 >7:return True
			if self.table[position] == self.table[position+1] == self.table[position+2]:
				self.table[position] = self.getColorCandy()
				return False
		elif direction == 'down':
			if position>89:return True
			if self.table[position] == self.table[position+10] == self.table[position+20]:
				self.table[position] = self.getColorCandy()
				return False

	def RefreshDetect(self):
		for position, value in self.table.items():
			if self.Refresh_patrol(position, 'right')==True or self.Refresh_patrol(position, 'down')==True:
				return
				
		print('origin table is impossible to play!')
		self.show()
		print('start refresh:')
		self.build()

	def Refresh_patrol(self, position, direction):
		if direction == 'right':
			if position%10 >6:return False
			# 取4個相鄰的糖果，如果可以成功交換,其比例必為3：1
			testField = collections.defaultdict(list)
			for i in range(position, position+4):
				testField[self.table[i]].append(i)
				if len(testField[self.table[i]]) == 3:
					print(testField)
					return True

		elif direction == 'down':
			if position>79:return False
			if self.table[position] == self.table[position+10] == self.table[position+20]:
				self.table[position] = self.getColorCandy()
				return True
			# 取4個相鄰的糖果，如果可以成功交換,其比例必為3：1
			testField = collections.defaultdict(list)
			for i in range(position, position+40, 10):
				testField[self.table[i]].append(i)
				if len(testField[self.table[i]]) == 3:
					return True

	def build(self):
		for i in range(1, self.length+1):
			for j in range(0, self.width):
				self.table[i*10+j] = self.getColorCandy()
		self.CollisionDetect()
		self.RefreshDetect()

	def main(self):
		self.numOfColor = int(input('how many color do you want?'))

		self.build()
		print('After refresh:')
		self.show()

	def show(self):
		for i in range(1, self.length+1):
			string = ''
			for j in range(0, self.width):
				string += self.table[i*10+j]
			print(string)

if __name__ == '__main__':
	c = Candycrush()
	c.main()
