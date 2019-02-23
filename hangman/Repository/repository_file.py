from Domain.sentence import Sentence


class RepositoryFile:
	def __init__(self, filename):
		self.__list = []
		self.__filename = filename

	def add(self, new_sentence):
		new_sentence = new_sentence.strip()

		parts = new_sentence.split()
		if len(parts) >= 3:
			sentence = Sentence(new_sentence)
			self.__list.append(sentence)

		self.writeToFile()

	def list(self):
		return self.__list

	def readFromFile(self):
		f = open(self.__filename, "r")

		line = f.readline()
		while len(line) > 0:
			self.add(line)
			line = f.readline()

		f.close()

	def writeToFile(self):
		f = open(self.__filename, "w")

		for element in self.list():
			f.write(element.string + '\n')

		f.close()






