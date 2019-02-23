class Sentence:
	def __init__(self, string):
		self.__string = string

	@property
	def string(self):
		return self.__string

	@string.setter
	def string(self, newString):
		self.__string = newString

	def __str__(self):
		return self.__string
