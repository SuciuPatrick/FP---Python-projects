"""
- read all the imformation about ski jumps from file(jumps.txt)
- give back the gold silver and bronze winners and their jumps distance.
- plot jumps in a file in the following way.

- tests and specs
"""


class Ski:
	def __init__(self, name, time_air, average_speed, wind_speed):
		self.__name = name
		self.__time_air = time_air
		self.__average_speed = average_speed
		self.__wind_speed = wind_speed
		self.__distance = 0

	@property
	def name(self):
		return self.__name

	@property
	def time_air(self):
		return self.__time_air

	@property
	def average_speed(self):
		return self.__average_speed

	@property
	def wind_speed(self):
		return self.__wind_speed

	@property
	def distance(self):
		return self.__distance

	def set_distance(self, distance):
		self.__distance = distance


	def __str_(self):
		return "Name: " + self.__name + "Time in air: " + str(self.__time_air) + "Average speed: " + str(self.__average_speed) + "wind_speed: " + str(self.__wind_speed)


def testSki():
	ski = Ski("Patr", 1, 2, 3)

	assert ski.name == "Patr"
	assert ski.time_air == 1
	assert ski.average_speed == 2