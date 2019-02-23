from add_insert import add

def calcAverage(participant):
	"""
	Returns the average scores of a participant
	:param participant: dictionary
	:return: float
	"""
	return (participant['p1'] + participant['p2'] + participant['p3']) / 3


def listCompare(listOfParticipants, sign, value):
	"""
	:param listOfParticipants: list
	:param sign: string
	:param value: integer
	:return: none
	"""
	if sign == '=':
		for part in listOfParticipants:
			if calcAverage(part) == value:
				print(part['p1'], part['p2'], part['p3'])
	elif sign == '<':
		for part in listOfParticipants:
			if calcAverage(part) < value:
				print(part['p1'], part['p2'], part['p3'])

	elif sign == '>':
		for part in listOfParticipants:
			if calcAverage(part) > value:
				print(part['p1'], part['p2'], part['p3'])

def equals(listOfParticipants):
	"""
	copy what is in listOfParticipants and put it into newList
	:param listOfParticipants: list
	:return: list
	"""

	newList = []
	for part in listOfParticipants:
		add(newList, part)

	return newList

def sortList(listOfParticipants):
	"""

	Sorts the list.

	:param listOfParticipants: list
	:return: list
	"""
	newListOfParticipants = equals(listOfParticipants)
	n = len(newListOfParticipants)
	i = 0

	while i < n - 1:
		j = i + 1
		while j < n:
			if calcAverage(newListOfParticipants[i]) < calcAverage(newListOfParticipants[j]):
				newListOfParticipants[i], newListOfParticipants[j] = newListOfParticipants[j], newListOfParticipants[i]
			j += 1
		i += 1

	return newListOfParticipants
