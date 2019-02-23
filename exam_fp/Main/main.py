from Repo.RepositoryText import RepositoryTextFile
from Service.Controller import Controller
from UI.UserInterface import UserInterface
from Domain.Ski import testSki

class Main:
	def __init__(self):
		pass
	def runTest(self):
		testSki()

	def runApp(self):
		repo = RepositoryTextFile("/Users/suciupatrick/UBB-Info/FP-courses/exam_fp/jumps.txt")
		repo.writeToFile()
		controller = Controller(repo)
		ui = UserInterface(controller)

		ui.showMenu()
		while True:
			value = input("Insert command -> ")

			if value == "1":
				ui.displayTop3()
			if value == "2":
				repo.writeToFile()


x = Main()
x.runTest()
x.runApp()