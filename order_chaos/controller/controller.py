from texttable import Texttable
import random

class Controller:
	def __init__(self, repository):
		self.__repository = repository

	def printBoard(self):
		texttable = Texttable()
		for i in self.__repository.board:
			texttable.add_row(i)

		return texttable.draw()

	def movePlayer(self, i, j, sign):
		mat = self.__repository.board

		if self.__repository.setPiece(i, j, sign) == False:
			return False
		return True

	def verificareLinie(self, i, j):
		cnt = 1

		auxJ = j - 1
		while  auxJ >= 0 and self.__repository.board[i][auxJ] == 'O':
			auxJ -= 1
			cnt += 1

		auxJ = j + 1
		while auxJ <= 5 and self.__repository.board[i][auxJ] == 'O':
			auxJ += 1
			cnt += 1

		if cnt == 5:
			return cnt
		return cnt

	def verificareColoana(self, i, j):
		cnt = 1

		auxJ = j - 1
		while  auxJ >= 0 and self.__repository.board[auxJ][j] == 'O':
			auxJ -= 1
			cnt += 1

		auxJ = j + 1
		while auxJ <= 5 and self.__repository.board[auxJ][j] == 'O':
			auxJ += 1
			cnt += 1

		if cnt == 5:
			return cnt
		return cnt

	def linieFull(self, i):
		cnt = 0
		for nr in range(0, 6):
			if self.__repository.board[i][nr] == ' ':
				cnt += 1

		if cnt == 0:
			return True
		return False

	def coloanaFull(self, i):
		cnt = 0

		for nr in range(0, 6):
			if self.__repository.board[nr][i] == ' ':
				cnt += 1

		if cnt == 0:
			return True
		return False

	def computerWon(self):
		for i in range(0, 6):
			for j in range(0, 6):
				if self.__repository.board[i][j] == ' ':
					return False

		return True

	def computerPosition(self):
		ok = False
		for j in range(0, 6):
			if self.verificareColoana(0, j) >= 3 and self.coloanaFull(j) is False:
				i = random.randint(0, 5)
				while self.movePlayer(i, j, 'X') == False:
					i = random.randint(0, 5)
				ok = True
				break

		if ok == False:
			for j in range(0, 6):
				if self.verificareLinie(j, 0) >= 3 and self.linieFull(j) is False:
					i = random.randint(0, 5)
					while self.movePlayer(j, i, 'X') == False:
						i = random.randint(0, 5)
					ok = True
					break

		if ok == False:
			i = random.randint(0, 5)
			j = random.randint(0, 5)
			while self.movePlayer(i, j, 'X') == False:
				i = random.randint(0, 5)
				j = random.randint(0, 5)

