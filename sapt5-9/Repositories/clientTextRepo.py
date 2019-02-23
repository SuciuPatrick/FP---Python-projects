from Domain.Client import Client
from Repositories.repository import Repository


class ClientTextRepo(Repository):
	def __init__(self, fileName):
		Repository.__init__(self)
		self._fileName = fileName

	def writeToFile(self):
		try:
			f = open(self._fileName, "w")
			for client in Repository.getList(self):
				f.write(str(client.id) + ";" + client.name)

			f.close()
		except:
			pass

	def readFromFile(self):
		try:
			f = open(self._fileName, "r")
			line = f.readline()

			while len(line) > 0:
				parts = line.split(";")
				client = Client(int(parts[0]), parts[1])
				Repository.add(self, client)
				line = f.readline()

			f.close()
		except:
			pass

	def add(self, client):
		Repository.add(self, client)
		self.writeToFile()

	def remove(self, idClient):
		if Repository.findByAnID(self, idClient) != -1:
			x = Repository.getList(self)
			del x[idClient]
		self.writeToFile()

	def update(self, position, objectt):
		Repository.update(self, position, objectt)
		self.writeToFile()


