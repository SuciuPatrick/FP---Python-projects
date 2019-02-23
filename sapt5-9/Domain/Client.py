class Client:
	def __init__(self, clientId, name):
		self._name = name
		self._id = clientId

	@property
	def id(self):
		return self._id

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, name):
		self._name = name

	def __eq__(self, other):
		return self._id == other._id and self._name == other._name

	def __str__(self):
		return "ID: " + str(self._id) + " Name = " + str(self._name)
		#return str(self._id) + ";" + str(self._name)