# coding=utf-8
from __future__ import absolute_import
import random, collections
class CandyTable(object):
	u"""docstring for candycrush"""
	def __init__(self, length, width):
		self.length, self.width = length, width
		self.numOfColor = None
		self.round = 20
		self.Color = [u'0;31;40', u'0;32;40', u'0;33;40', u'0;34;40', u'0;35;40', u'0;36;40', u'0;37;40', u'0;30;41', u'0;32;41', u'0;33;41', u'0;34;41', u'0;35;41', u'0;36;41', u'0;37;41', u'0;30;42', u'0;31;42', u'0;33;42', u'0;34;42', u'0;35;42', u'0;36;42', u'0;37;42', u'0;30;43', u'0;31;43', u'0;32;43', u'0;34;43', u'0;35;43', u'0;36;43', u'0;37;43', u'0;30;44', u'0;31;44', u'0;32;44', u'0;33;44', u'0;35;44', u'0;36;44', u'0;37;44']
		self.table = {}
		self.cancelSet = set()
		self.point = 0

	def exchange(self, x, y):
		self.table[x], self.table[y] = self.table[y], self.table[x]

	def getColorCandy(self):
		# get Colorful Candy in random order
		return u'\x1b[{}m 🍬 \x1b[0m'.format(self.Color[random.randint(0, self.numOfColor-1)])

	def CollisionDetect(self, callback):
		# onlyCheck means:if you don't want to correct this map
		# only want to check if there is three candy in a line
		# then set onlyCheck = True
		# onlyCheck = True will not do recursive.
		# if three candys in a line, then return True
		# means Detect Collision.
		for position, value in self.table.items():
			if self.Collision_patrol(position, u'right'):
				if callback(position, u'right'): return True
				
			if self.Collision_patrol(position, u'down'):
				if callback(position, u'down'): return True

	def Collision_patrol(self, position, direction):
		# onlyCheck means:if you don't want to correct this map
		# only want to check if there is three candy in a line
		# then set onlyCheck = True
		# onlyCheck = True means won't set a new candy into map.
		# only detect.
		if direction == u'right':
			# set position%10 > 7 because i only check there is three candy in vertical lines.
			# which means position+0~position+2 should be same color
			# so need an upper bound
			# position+2 cannot exceed limits of map!!!
			if position%10 >7:return False
			if self.table[position] == self.table[position+1] == self.table[position+2]:
				return True
		elif direction == u'down':
			if position>89:return False
			if self.table[position] == self.table[position+10] == self.table[position+20]:
				return True

	def RefreshDetect(self):
		# Detect if there is any possibility to make three same color candy in a line.
		for position, value in self.table.items():
			if self.Refresh_patrol(position, u'right') or self.Refresh_patrol(position, u'down'):
				return

		print(u'origin table is impossible to play!')
		self.show()
		print(u'after refresh:')
		self.build()

	def Refresh_patrol(self, position, direction):
		# exchange candy in horizontally and vertically.
		# and then use CollisionDetect to check if there is three candy in a line.
		# if it does, then return True, means: it' possible to make this game start to play.
		# else: continue to check.

		# REMEMBER, those candys be exchanged need to be put back.
		if direction == u'right':
			if position%10 >8:return False

			self.exchange(position, position+1)
			if self.CollisionDetect(lambda x, y:True):
				self.exchange(position, position+1)
				return True
			else:
				self.exchange(position, position+1)

		elif direction == u'down':
			if position>99:return False

			self.exchange(position, position+10)
			if self.CollisionDetect(lambda x, y:True):
				self.exchange(position, position+10)
				return True
			else:
				self.exchange(position, position+10)

	def build(self):
		# generat table in random order
		# and then use CollisoinDetect to check map has no three candys in a line.
		# also use RefreshDetect to check it's still possible to play this game.
		for i in xrange(1, self.length+1):
			for j in xrange(0, self.width):
				self.table[i*10+j] = self.getColorCandy()

		def assignCandy(position, direction):
			self.table[position] = self.getColorCandy()
			self.CollisionDetect(assignCandy)

		self.CollisionDetect(assignCandy)
		self.RefreshDetect()

	def main(self):
		self.numOfColor = int(raw_input(u'how many color do you want?'))

		self.build()
		self.show()
		
		# start to play
		def CancelScore(position, direction):
			if direction == u'right':
				self.cancelSet.add(position)
				self.cancelSet.add(position+1)
				self.cancelSet.add(position+2)
			elif direction == u'down':
				self.cancelSet.add(position)
				self.cancelSet.add(position+10)
				self.cancelSet.add(position+20)

		def falldown():
			self.point += len(self.cancelSet)
			self.cancelSet = sorted(self.cancelSet)
			print(u'被消去的糖果的座標:{}'.format(self.cancelSet))
			self.show()

			for i in self.cancelSet:
				while i-10>=10:
					self.table[i] = self.table[i-10]
					i -= 10
				self.table[i] = self.getColorCandy()

			self.cancelSet = set()
			self.CollisionDetect(CancelScore)
			if len(self.cancelSet) > 0:
				falldown()

		print(u'本系統座標系不太一樣請注意！！！')
		print(u'左上角是 1,0(輸入時請輸入10)')
		print(u'右下角是10,9(輸入時請輸入109)'	)
		print(u'X座標為0~9 Y座標為1~10')
		for i in xrange(self.round):
			origin  = int(raw_input(u'please input first coordinate you want to exchange:'))
			exchange = int(raw_input(u'please input first coordinate you want to exchange:'))
			self.exchange(origin, exchange)

			self.CollisionDetect(CancelScore)
			if len(self.cancelSet) > 0:
				falldown()
			else:
				print(u'invalid exchage!!!')
				self.exchange(origin, exchange)
			
			print(u'Round {}:you got {} points'.format(i+1, self.point))
			self.show()

			self.RefreshDetect()

		print(u'Your final score is {}'.format(self.point))

	def show(self):
		for i in xrange(1, self.length+1):
			string = u''
			for j in xrange(0, self.width):
				string += self.table[i*10+j]
			print(string)

if __name__ == u'__main__':
	c = CandyTable(10, 10)
	c.main()
