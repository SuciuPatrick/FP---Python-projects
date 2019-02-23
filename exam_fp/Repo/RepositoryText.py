from Repo.Repository import Repository
from Domain.Ski import Ski


class RepositoryTextFile(Repository):
	def __init__(self, text_file):
		Repository.__init__(self)
		self.__textFile = text_file
		self.readFromFile()

	def readFromFile(self):
		try:
			f = open(self.__textFile, "r")
			line = f.readline()
			while len(line) > 0:
				line = line.strip()
				parts = line.split(",")

				skier = Ski(parts[0], float(parts[1]), int(parts[2]), int(parts[3]))
				Repository.add(self, skier)
				line = f.readline()
			f.close()
		except IOError as e:
			raise SyntaxError("Cannot load file - " + str(e))

	def writeToFile(self):
		try:
			f = open("/Users/suciupatrick/UBB-Info/FP-courses/exam_fp/stelute.txt", "w")
			for skier in self.getList():
				calc = 0
				dist = skier.time_air * (skier.average_speed  * skier.average_speed + skier.wind_speed)
				while calc < dist:
					f.write("*")
					calc += 100
				f.write(skier.name)
		except IOError as e:
			raise SyntaxError("Cannot load file - " + str(e))