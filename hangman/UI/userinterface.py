from Domain.sentence import Sentence
from Repository.repository_file import RepositoryFile

class UI():
	def __init__(self, controller):
		self.__controller = controller

	def showMenu(self):
		print("\t\t~HANGMAN~")
		print("\t1. Add new sentence to the game.")
		print("\t2. Play hangman")

	def addUI(self):
			value = input("-> Insert new sentence: ")
			self.__controller.addSentence(value)

	def playGame(self):
		pozitieString = self.__controller.chooseRandom()
		initialStr = self.__controller.formStartingString(pozitieString)
		print(self.__controller.printStringFromList(initialStr))
		pozitie = 0
		hangman = ""
		while True:
			value = input("try me bitch: ")
			x = self.__controller.verificareLitera(initialStr, pozitieString, value)
			if len(x) == 0:
				if hangman == "sugipula":
					print("You lost go kill yourself.")
					return

				hangman = self.__controller.verificarePierdere(pozitie, hangman)

				pozitie += 1
				print(self.__controller.printStringFromList(initialStr) + "    " + hangman)
			else:
				print (self.__controller.printStringFromList(x) + "    " + hangman)