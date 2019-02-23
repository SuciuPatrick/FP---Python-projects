# Setters
def setP1(dictionar, P1):
	"""
	:param dictionar: dictionary
	:param P1: integer
	:return: none
	"""
	dictionar["p1"] = P1


def setP2(dictionar, P2):
	"""
	:param dictionar: dictionary
	:param P2: integer
	:return: none
	"""
	dictionar["p2"] = P2


def setP3(dictionar, P3):
	"""
	:param dictionar: dictionary
	:param P3: integer
	:return: none
	"""
	dictionar["p3"] = P3


# End of setters

def constructorScore(P1, P2, P3):
	"""
	Creates a dictionary that contains the scores of a student.

	:param P1: integer
	:param P2: integer
	:param P3: integer

	output: dictionary
	"""
	participant = {"p1": 0, "p2": 0, "p3": 0}
	setP1(participant, P1)
	setP2(participant, P2)
	setP3(participant, P3)

	return participant


def add(listOfParticipants, participant):
	"""
	Add an element(dictionary) to the list

	:param listOfParticipants: list
	:param participant: dictionary
	:return: none
	"""
	listOfParticipants.append(participant)


def insert(listOfParticipants, participant, position):
	"""
	:param listOfParticipants: list
	:param participant: dictionary
	:param position: integer
	:return: none
	"""
	listOfParticipants.insert(position, participant)


def addForTests(listOfParticipants):
	add(listOfParticipants, constructorScore(1, 2, 3))
	add(listOfParticipants, constructorScore(3, 4, 5))
	add(listOfParticipants, constructorScore(10, 13, 15))