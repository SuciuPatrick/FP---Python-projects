from random import randint
from Domain.Ski import Ski


class Repository:
	def __init__(self):
		self.__l = []

	def add(self, skier):
		self.__l.append(skier)

	def getList(self):
		return self.__l

	def calculateDistance(self, skier):
		return skier.time_air * (skier.average_speed  * skier.average_speed + skier.wind_speed)

def repoTests():
	repo = Repository()
	skier = Ski("Patrick", 1, 2, 3)
	repo.add(skier)

	x = repo.getList()



