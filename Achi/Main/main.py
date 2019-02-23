from Repo.repository import Repository
from Controller.controller import Controller
from UI.user_interface import UI

import texttable

class Main:
	def __init__(self):
		pass

	def startapp(self):
		repo = Repository()
		controller = Controller(repo)
		ui = UI(controller)

		ui.startGame()




start = Main()
start.startapp()