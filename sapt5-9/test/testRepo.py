from Repositories.repository import *
import unittest


class repoTest(unittest.TestCase):
	def initialize(self):
		self.clientRepo = Repository()
		self.movieRepo = Repository()

	def testClientRepo(self):
		c1 = Client(1, "Marcu")
		self.clientRepo.add(c1)
		self.assertTrue(c1 in self.clientRepo.getList())
		c3 = Client(5, "Marcus")
		self.assertTrue(len(self.clientRepo.getList()) == 1)
		self.clientRepo.add(c3)
		self.assertTrue(c3 == self.clientRepo.getList()[1])
		self.assertTrue(len(self.clientRepo.getList()) == 2)
		c2 = Client(3, "M")
		self.clientRepo.add(c2)
		self.assertTrue(c2 == self.clientRepo.getList()[1])
		self.assertTrue(self.clientRepo.findByID(Client(3, "M")))
		self.assertFalse(self.clientRepo.findByID(Client(4, "A")))
		self.assertTrue(self.clientRepo.findByAnID(3))
		self.assertTrue(self.clientRepo.findPosByID(5) == 2)
		self.assertTrue(self.clientRepo.findObj(5) == Client(5, "Marcus"))
		self.assertTrue(self.clientRepo.findObj(7) == None)
		self.clientRepo.remove(1)
		self.assertTrue(c1 not in self.clientRepo.getList())
		self.clientRepo.remove(5)
		self.assertTrue(c3 not in self.clientRepo.getList())

	def testMovieRepo(self):
		m1 = Movie(1, "a", 'b', 'c')
		self.movieRepo.add(m1)
		self.assertTrue(m1 in self.movieRepo.getList())
		m3 = Movie(5, "d", 'e', 'f')
		self.assertTrue(len(self.movieRepo.getList()) == 1)
		self.movieRepo.add(m3)
		self.assertTrue(m3 == self.movieRepo.getList()[1])
		self.assertTrue(len(self.movieRepo.getList()) == 2)
		m2 = Movie(3, "g", 'h', 'i')
		self.movieRepo.add(m2)
		self.assertTrue(m2 == self.movieRepo.getList()[1])
		self.movieRepo.remove(1)
		self.assertTrue(m1 not in self.movieRepo.getList())
		self.movieRepo.remove(5)
		self.assertTrue(m3 not in self.movieRepo.getList())

def callRepoTest():
	Test = repoTest()

	Test.initialize()
	Test.testClientRepo()
	Test.testMovieRepo()