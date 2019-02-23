from list import calcAverage

def avg(listOfParticipants, start, end):
	"""
	Return the average score from start to end(indexes)
	:param listOfParticipants: list
	:param start: integer
	:param end: integer
	:return: float
	"""

	cnt = 0
	x = 0
	while start <= end:
		x = x + calcAverage(listOfParticipants[start])
		cnt += 1
		start += 1
	return x / cnt

def calcMinim(listOfParticipants, start, end):
	"""
	Returns the lowest average score from start<=end

	:param listOfParticipants: list
	:param start: integer
	:param end: integer
	:return: float
	"""
	minim = 11
	print('k')
	while start <= end:
		if minim > calcAverage(listOfParticipants[start]):
			minim = calcAverage((listOfParticipants[start]))
		start += 1
	return minim
