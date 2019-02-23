from controller.controller import Controller
from repository.repository_board import Repository
from user_interface.ui import UI

class Main:
	def __init__(self):
		pass

	def startapp(self):
		repo = Repository("")
		controller = Controller(repo)
		ui = UI(controller)

		ui.printInstructions()

		value = input("insert a command -> ")
		if value == '1':
			ui.newGame()


start = Main()
start.startapp()