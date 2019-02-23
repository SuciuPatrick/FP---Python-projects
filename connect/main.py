from texttable import Texttable
from random import randint

class Board:
	def __init__(self):
		self.data = [[' '] * 6, [' '] * 6, [' '] * 6, [' '] * 6, [' '] * 6, [' '] * 6]

	def printBoard(self):
		textTable = Texttable()

		n = len(self.data)
		for i in range(n):
			textTable.add_row(self.data[i])

		print(textTable.draw())

	def setPosition(self, col, piece):
		n = len(self.data)
		n -= 1
		while n >= 0:
			if self.data[n][col] == ' ':
				self.data[n][col] = piece
				return n
			n -= 1

	def getLine(self, col):
		# returneaza lini a de pe ultima coloana
		n = len(self.data)
		n -= 1

		i = 0
		while i <= n:
			if self.data[i][col] != ' ':
				return i
			i += 1

	def verification(self, row, col):
		n = len(self.data)
		n -= 1

		# verificare pe coloana
		cnt = 0
		i = row
		j = col
		while i <= n - 1 and self.data[i][j] == self.data[i + 1][j]:
			cnt += 1
			i += 1

		if cnt >= 3:
			return True

		# verificare pe linie
		cnt = 0
		i = row
		j = col

		while j <= n - 1 and self.data[i][j] == self.data[i][j + 1]:
			cnt += 1
			j += 1

		i = row
		j = col
		while i > 0 and self.data[i][j] == self.data[i][j - 1]:
			cnt += 1
			j -= 1

		if cnt >= 3:
			return True

		#verificare pe diagonala
		i = row
		j = col
		cnt = 0
		while i <= n - 1 and j <= n - 1 and self.data[i][j] == self.data[i + 1][j + 1]:
			cnt += 1
			i += 1
			j += 1

		i = row
		j = col
		while i > 0 and j > 0 and self.data[i][j] == self.data[i - 1][j - 1]:
			cnt += 1
			i -= 1
			j -= 1

		if cnt >= 3:
			return True

		# verificare pe diagonala part 2
		i = row
		j = col
		cnt = 0
		while i <= n - 1 and j > 0 and self.data[i][j] == self.data[i + 1][j - 1]:
			cnt += 1
			i += 1
			j -= 1

		i = row
		j = col
		while i > 0 and j <= n - 1 and self.data[i][j] == self.data[i - 1][j + 1]:
			cnt += 1
			i -= 1
			j += 1

		if cnt >= 3:
			return True
		return False


matrice = Board()

print("Computer = 1          Human = 2")
value = input("Choose the game mode: ")
while True:

	if value == '2':
		position = int(input("Player 1 position -> "))
		linie = matrice.setPosition(position, 'X')
		if matrice.verification(linie, position) is True:
			matrice.printBoard()
			print("Player 1 won.")
			break
		matrice.printBoard()

		position2 = int(input("Player 2 position -> "))
		linie2 = matrice.setPosition(position2, 'O')
		if matrice.verification(linie2, position2) is True:
			matrice.printBoard()
			print ("Player 2 won.")
			break
		matrice.printBoard()

	elif value == '1':
		position = int(input("Choose a position -> "))
		linie = matrice.setPosition(position, 'X')
		if matrice.verification(linie, position) is True:
			matrice.printBoard()
			print("You won.")
			break

		position2 = randint(0, 5)
		linie2 = matrice.setPosition(position2, 'O')

		if matrice.verification(linie2, position) is True:
			matrice.printBoard()
			print("Computer won.")
			break

		matrice.printBoard()