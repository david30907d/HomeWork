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

	def exchange(self, x, y):
		self.table[x], self.table[y] = self.table[y], self.table[x]

	def getColorCandy(self):
		return '\x1b[{}m 🍬 \x1b[0m'.format(self.Color[random.randint(0, self.numOfColor-1)])

	def CollisionDetect(self, onlyCheck):
		# onlyCheck means:if you don't want to correct this map
		# only want to check if there is three candy in a line
		# then set onlyCheck = True
		# onlyCheck = True will not do recursive.
		# if three candys in a line, then return True
		# means Detect Collision.
		for position, value in self.table.items():
			if self.Collision_patrol(position, 'right', onlyCheck):
				if onlyCheck:return True
				self.CollisionDetect(onlyCheck)
			if self.Collision_patrol(position, 'down', onlyCheck):
				if onlyCheck:return True
				self.CollisionDetect(onlyCheck)

	def Collision_patrol(self, position, direction, onlyCheck):
		# onlyCheck means:if you don't want to correct this map
		# only want to check if there is three candy in a line
		# then set onlyCheck = True
		# onlyCheck = True means won't set a new candy into map.
		# only detect.
		if direction == 'right':
			# set position%10 > 7 because i only check there is three candy in vertical lines.
			# which means position+0~position+2 should be same color
			# so need an upper bound
			# position+2 cannot exceed limits of map!!!
			if position%10 >7:return False
			if self.table[position] == self.table[position+1] == self.table[position+2]:
				if onlyCheck==False: self.table[position] = self.getColorCandy()
				return True
		elif direction == 'down':
			if position>89:return False
			if self.table[position] == self.table[position+10] == self.table[position+20]:
				if onlyCheck==False: self.table[position] = self.getColorCandy()
				return True

	def RefreshDetect(self):
		for position, value in self.table.items():
			if self.Refresh_patrol(position, 'right') or self.Refresh_patrol(position, 'down'):
				return
				
		print('origin table is impossible to play!')
		self.show()
		self.build()

	def Refresh_patrol(self, position, direction):
		if direction == 'right':
			if position%10 >8:return False

			self.exchange(position, position+1)
			if self.CollisionDetect(onlyCheck=True):
				self.exchange(position, position+1)
				return True
			else:
				self.exchange(position, position+1)

		elif direction == 'down':
			if position>99:return False

			self.exchange(position, position+10)
			if self.CollisionDetect(onlyCheck=True):
				self.exchange(position, position+10)
				return True
			else:
				self.exchange(position, position+10)

	def build(self):
		for i in range(1, self.length+1):
			for j in range(0, self.width):
				self.table[i*10+j] = self.getColorCandy()
		self.CollisionDetect(onlyCheck=False)
		self.RefreshDetect()

	def main(self):
		self.numOfColor = int(input('how many color do you want?'))

		self.build()
		print('After refresh:')
		self.show()
		print(self.table)

	def show(self):
		for i in range(1, self.length+1):
			string = ''
			for j in range(0, self.width):
				string += self.table[i*10+j]
			print(string)

if __name__ == '__main__':
	c = Candycrush()
	c.main()
