from repository.repository_board import Repository
from controller.controller import Controller

class UI:
	def __init__(self, controller):
		self.__controller = controller

	def printInstructions(self):
		print("1. New game.")
		print("2. Load from text.")

	def newGame(self):
		print (self.__controller.printBoard())

		while True:
			try:
				i = int(input("i: "))
				j = int(input("j: "))
				if self.__controller.movePlayer(i, j, 'O') == False:
					print("Not a valid position.")
				else:
					self.__controller.computerPosition()
					print(self.__controller.printBoard())

				if self.__controller.computerWon() is True:
					print("COMPUTER WON. HAHAHA")
					break

				if self.__controller.verificareLinie(i, j) >= 5 or self.__controller.verificareColoana(i, j) >= 5:
					print("PLAYER WON.")
					break


			except ValueError:
				print("i and j must be integer. ")



