from list import equals
from add_insert import add

def nullList(listOfParticipants):
	"""
	It makes the list null

	:param listOfParticipants: list
	:return: none
	"""
	index = 0
	n = len(listOfParticipants)
	while index < n:
		del listOfParticipants[0]
		index += 1


def undo(listOfParticipants, backupParticipants):
	"""
	Undo one operation that was made
	:param listOfParticipants: list
	:param backupParticipants: list
	:return: none
	"""
	n = len(backupParticipants)

	nullList(listOfParticipants)
#	print(listOfParticipants)
#	print(backupParticipants)
	for part in backupParticipants[n - 1]:
		add(listOfParticipants, part)

	del backupParticipants[n - 1]