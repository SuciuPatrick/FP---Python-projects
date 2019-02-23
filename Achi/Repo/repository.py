from texttable import Texttable

class Repository:
	def __init__(self):
		self.__board = [3 * [' '], 3 * [' '], 3 * [' ']]

	def createBeatifulBoard(self):
		table = Texttable()

		for a in self.__board:
			table.add_row(a)

		return table.draw()

	@property
	def board(self):
		return self.__board