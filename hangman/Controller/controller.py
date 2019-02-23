import random


class Controller:
	def __init__(self, repository):
		self.__repository = repository

	@property
	def repository(self):
		return self.__repository

	def addSentence(self, str):
		self.__repository.add(str)

	def chooseRandom(self):
		"""
			returns a random string to start the game
		"""
		lst = self.__repository.list()
		x = random.randint(0, len(lst) - 1)
		return x

	def formStartingString(self, randomIndex):
		repo = self.__repository.list()
		elem = repo[randomIndex]

		strNull = []
		n = len(elem.string) - 1
		i = 0
		while i <= n:
			if elem.string[0] == elem.string[i] or elem.string[i] == elem.string[n]:
				strNull.append(str(elem.string[i]))
			elif elem.string[i] == ' ':
				strNull.append(' ')
			else:
				strNull.append('_')
			i += 1

		return strNull #list de prelucrat

	def printStringFromList(self, list):

		strAfisare = ""
		for a in list:
			strAfisare = strAfisare + str(a)

		return strAfisare

	def verificareLitera(self, list, pozitieRepo, char):

		i = 0
		n = len(list) - 1
		repo  = self.__repository.list()
		ok = 0
		list0 = []
		lstRepo = repo[pozitieRepo].string
		while i <= n:
			if lstRepo[i] == char:
				ok = 1
				list[i] = char
			i += 1
		if ok == 1:
			return list
		else:
			return list0

	def verificarePierdere(self, pozitie, str):
		hangman = "sugipula"

		return str + hangman[pozitie]

