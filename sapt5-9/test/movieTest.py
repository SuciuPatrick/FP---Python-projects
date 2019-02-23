from Domain.Movie import *
import unittest

class testMovie(unittest.TestCase):
	def initialize(self):
		self.mov = Movie(1, "Bla Bla", "Don't watch it with your mother.", "Drama")
		self.mov2 = Movie(2, "Bla Bla", "Dont", "Action")

	def testMovie(self):
		self.assertTrue(self.mov == Movie(1, "Bla Bla", "Don't watch it with your mother.", "Drama"))
		self.assertTrue(self.mov2 == Movie(2, "Bla Bla", "Dont", "Action"))
		self.assertTrue(self.mov.description == "Don't watch it with your mother.")
		self.assertTrue(self.mov.id == 1)
		self.assertTrue(self.mov2.genre == "Action")

def callTestMovie():
	Test = testMovie()

	Test.initialize()
	Test.testMovie()