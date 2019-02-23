from Service import Controller


class UserInterface:
	def __init__(self, controller):
		self.__controller = controller

	@staticmethod
	def showMenu():
		print("1. give medals.")
		print("2. Plot the distance")

	def displayTop3(self):
		self.__controller.top()
		x = self.__controller.medals()

		index = 0

		for skier in x:
			print(str(skier.name) + " with distance " + str(skier.distance))
			index += 1
			if index == 3:
				break





