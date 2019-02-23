"""
authors = ["Suciu Patrick", "Suciu Andrei", "Robert Cristian", "Cosmulei Patric"]

authors.sort(key = lambda name: name.split(' ')[0].lower())

#print(authors)

a = lambda x: [x + 1]
b = a(1)
c = lambda x: x + b
d = c([1])
a=1
b=3
print (a, b, c(4), d[1])
"""
import unittest
def sumList(lst):
	"""

	:param list:
	:return:
	"""
	suma = 0
	if type(lst) is not list:
		raise TypeError

	for a in lst:
		if a % 2 == 0:
			suma += a

	if suma == 0:
		raise ValueError
	return suma


class TestCalc(unittest.TestCase):
	def test_sum(self):
		self.assertEqual(sumList([2, 8]), 10)
		self.assertEqual(sumList([2, 8]), 10)
		self.assertEqual(sumList([2, 8]), 10)
		self.assertEqual(sumList([2, 8]), 10)
		self.assertRaises(ValueError, sumList, [0])



if __name__ == '__main__':
	unittest.main()

print ("okdd")
print("k")