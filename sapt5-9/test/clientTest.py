import unittest
from Domain.Client import *


class TestClient(unittest.TestCase):
	def initialize(self):
		self.c = Client(1, "Marcel Pavel")
		self.c1 = Client(1, "Marcel Pavel")

	def testClient(self):
		self.assertTrue(self.c == Client(1, "Marcel Pavel"))
		self.assertTrue(self.c.__str__() == "ID: 1 Name = Marcel Pavel")
		self.assertTrue(self.c.id == 1)
		self.assertTrue(self.c.name == "Marcel Pavel")
		self.assertTrue(self.c.__eq__(self.c1))


def callTestClient():
	#Test = TestClient()

	#Test.initialize()
	#Test.testClient()
	pass