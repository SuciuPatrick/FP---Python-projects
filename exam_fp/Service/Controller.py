from Domain.Ski import Ski
import operator

class Controller:
	def __init__(self, repository):
		self.__repository = repository

	@property
	def repository(self):
		return self.__repository

	def top(self):
		for skier in self.__repository.getList():
			distance = self.__repository.calculateDistance(skier)
			skier.set_distance(distance)

	def medals(self):
		x = self.__repository.getList()

		sorted_x = sorted(x, key=operator.attrgetter('distance'), reverse=True)

		return sorted_x


