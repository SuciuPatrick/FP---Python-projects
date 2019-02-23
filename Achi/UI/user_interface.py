class UI:
	def __init__(self, controller):
		self.__controller = controller

	def startGame(self):
		print(self.__controller.repository.createBeatifulBoard())
		while True:
			try:
				i = int(input("i -> "))
				j = int(input("j-> "))
				if i > 2 or j > 2:
					raise ValueError

				if self.__controller.makeMove(i, j, 'O') is False: #mutare player
					raise SyntaxError
				self.__controller.computerMove() #mutare computer
				if self.__controller.checkLine('O') is True or self.__controller.checkColumn('O') is True \
						or self.__controller.checkPrincipalDiagonal('O') is True or self.__controller.checkSecondDiagonal('O') is True:
					print ("Humar won.")
					print(self.__controller.repository.createBeatifulBoard())
					break
				elif self.__controller.checkLine('X') is True or self.__controller.checkColumn('X') is True \
						or self.__controller.checkPrincipalDiagonal('X') is True or self.__controller.checkSecondDiagonal('X') is True:
					print ("Computer Won.")
					print(self.__controller.repository.createBeatifulBoard())
					break
				elif self.__controller.numberSpaces() is True:
					print("The board is full. The computer has the change to win.")
					self.__controller.repository.createBeatifulBoard()
					self.__controller.chanceComputer()
					if self.__controller.checkLine('X') is True or self.__controller.checkColumn('X') is True \
							or self.__controller.checkPrincipalDiagonal('X') is True or self.__controller.checkSecondDiagonal('X') is True:
						print("Computer Won.")
						print(self.__controller.repository.createBeatifulBoard())
						break




				print (self.__controller.repository.createBeatifulBoard())
			except ValueError:
				print("Insert a valid input.")
			except SyntaxError:
				print("The space is taken.")


