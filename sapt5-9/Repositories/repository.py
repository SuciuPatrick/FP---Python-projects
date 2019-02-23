from Domain.Client import *
from Domain.Movie import *

class Repository:
	def __init__(self):
		self._list = []

	def add(self, newObject):
		ok = 0
		if len(self._list) > 0:
			if newObject.id < self._list[0].id:
				self._list.insert(0, newObject)
				ok = 1

		for i in range(0, len(self._list) - 1):
			if self._list[i].id < newObject.id < self._list[i + 1].id:
				self._list.insert(i + 1, newObject)
				ok = 1

		if ok == 0:
			self._list.append(newObject)

	def getList(self):
		return self._list

	def findByID(self, searchObject):
		for element in self._list:
			if element.id == searchObject.id:
				return True
		return False

	def findByAnID(self, findId):
		for element in self._list:
			if findId == element.id:
				return True
		return False

	def findPosByID(self, findId):
		index = 0
		for element in self._list:
			if findId == element.id:
				return index
			index += 1
		return -1

	def findObj(self, an_id):
		for element in self._list:
			if an_id == element.id:
				return element
		return None

	def remove(self, findId):
		i = self.findPosByID(findId)
		del self._list[i]

	def update(self, position, object):
		self[position] = object
