from texttable import Texttable

class Repository:
	def __init__(self, filename):
		self.__board = [6 * [' '], 6 * [' '], 6 * [' '], 6 * [' '], 6 * [' '], 6 * [' ']]
		self.__filename = filename

	@property
	def board(self):
		return self.__board

	@board.setter
	def board(self, newBoard):
		self.__board = newBoard

	def setPiece(self, i, j, sign):
		if self.__board[i][j] == ' ':
			self.__board[i][j] = sign
			return True
		return False




