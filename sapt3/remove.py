from add_insert import setP1, setP2, setP3

def removeParticipant(participant):
	"""
	Changes the scores of the participant and replace them with 0

	:param participant: dictionary
	:return: none
	"""
	setP1(participant, 0)
	setP2(participant, 0)
	setP3(participant, 0)

def removeParticipantsInterval(listOfParticipants, start, end):
	"""
	Changes the score of [start, end] indexes in the listOfParticipants to 0

	:param listOfParticipants: list
	:param start: integer
	:param end: integer
	:return: none
	"""
	while start <= end:
		setP1(listOfParticipants[start], 0)
		setP2(listOfParticipants[start], 0)
		setP3(listOfParticipants[start], 0)
		start += 1

def replaceScoreOfParticipant(participant, newScore, grade):
	"""
	Changes the grade of participant and replace with a new one. If the assigment failed it return false
	:param participant: dictionary
	:param newScore: integer
	grade: integer
	:return: boolean
	"""
	if grade == 'p1' or grade == 'P1':
		setP1(participant, newScore)
		return True
	elif grade == 'p2' or grade == 'P2':
		setP2(participant, newScore)
		return True
	elif grade == 'p3' or grade == 'P3':
		setP3(participant, newScore)
		return True
	return False

