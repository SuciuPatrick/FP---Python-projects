from list import equals

def sortListP(listOfParticipants, P):
	"""
	It sorts the list based on one of the scores.

	:param listOfParticipants: list
	:param P: string
	:return: list
	"""

	newListOfParticipants = equals(listOfParticipants)
	n = len(newListOfParticipants)
	i = 0

	while i < n - 1:
		j = i + 1
		while j < n:
			if newListOfParticipants[i][P] < newListOfParticipants[j][P]:
				newListOfParticipants[i], newListOfParticipants[j] = newListOfParticipants[j], newListOfParticipants[i]
			j += 1
		i += 1

	return newListOfParticipants
