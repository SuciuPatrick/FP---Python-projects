import random

class Controller:
	def __init__(self, repository):
		self.__repository = repository


	@property
	def repository(self):
		return self.__repository

	def makeMove(self, i, j, object):

		mat = self.__repository.board
		if mat[i][j] == ' ':
			mat[i][j] = object
		else:
			return False
		return True

	def checkLine(self, sign):
		mat = self.__repository.board
		for i in range (0, 3):
			cnt = 0
			for j in range(0, 3):
				if mat[i][j] == sign:
					cnt += 1
			if cnt == 3:
				return True
		return False

	def checkColumn(self, sign):
		mat = self.__repository.board

		for i in range(0, 3):
			cnt = 0
			for j in range(0, 3):
				if mat[j][i] == sign:
					cnt += 1

			if cnt == 3:
				return True
		return False

	def checkPrincipalDiagonal(self, sign):
		mat = self.__repository.board

		cnt = 0
		for i in range(0, 3):
			if mat[i][i] == sign:
				cnt += 1

		if cnt == 3:
			return True
		return False

	def checkSecondDiagonal(self, sign):
		mat = self.__repository.board

		cnt = 0
		n = 2
		for i in range(0, 3):
			if mat[i][n - i] == sign:
				cnt += 1

		if cnt == 3:
			return True
		return False

	def boardFull(self):
		mat = self.__repository.board

		for i in range(0, 3):
			for j in range(0, 3):
				if mat[i][j] == ' ':
					return False
		return True

	def computerMove(self):
		i = random.randint(0, 2)
		j = random.randint(0, 2)

		ok = False
		if self.boardFull() is False:
			while True:
				if self.makeMove(i, j, 'X') == True:
					return True
				i = random.randint(0, 2)
				j = random. randint(0, 2)
		return False

	def chanceComputer(self):
		mat = self.__repository.board

		indexLine = -1
		for i in range(0, 3):
			cnt = 0
			for j in range(0, 3):
				if mat[i][j] == 'X':
					cnt += 1
			if cnt == 2:
				indexLine = i
				break
		if indexLine != -1:
			for i in range(0, 3):
				if mat[indexLine][i] == 'O':
					mat[indexLine][i] = 'X'
					return True

	def numberSpaces(self):
		mat = self.__repository.board
		cnt = 0
		for i in range(0, 3):
			for j in range(0, 3):
				if mat[i][j] == ' ':
					cnt += 1

		if cnt == 1:
			return True
		return False





