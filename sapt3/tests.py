from add_insert import *
from remove import *
from list import calcAverage, equals
from avg_min import avg, calcMinim
from undo import undo

def tests():
	testAdd()
	testInsert()
	testRemoveParticipant()
	testRemoveParticipantsInterval()
	testReplaceScoreOfParticipant()
	testCalcAverage()
	testAvg()
	testCalcMinim()
	#testUndo()

def testAdd():
	contestParticipants = []
	add(contestParticipants, constructorScore(1, 2, 3))
	assert contestParticipants == [{"p1": 1, "p2": 2, "p3": 3}]

	add(contestParticipants, constructorScore(10, 4, 20))
	assert contestParticipants == [{"p1": 1, "p2": 2, "p3": 3}, {"p1": 10, "p2": 4, "p3": 20}]

	add(contestParticipants, constructorScore(3, 4, 5))
	assert contestParticipants == [{"p1": 1, "p2": 2, "p3": 3}, {"p1": 10, "p2": 4, "p3": 20},
	                               {"p1": 3, "p2": 4, "p3": 5}]


def testInsert():
	contestParticipants = []
	add(contestParticipants, constructorScore(1, 2, 3))
	add(contestParticipants, constructorScore(2, 3, 4))

	insert(contestParticipants, constructorScore(6, 9, 6), 1)
	assert contestParticipants[1] == {"p1": 6, "p2": 9, "p3": 6}

	insert(contestParticipants, constructorScore(3, 10, 2), 0)
	assert contestParticipants[0] == {"p1": 3, "p2": 10, "p3": 2}

def testRemoveParticipant():
	contestParticipants = []
	add(contestParticipants, constructorScore(1, 2, 3))
	add(contestParticipants, constructorScore(13, 20, 8))
	removeParticipant(contestParticipants[1])
	assert contestParticipants[1] == {"p1": 0, "p2": 0, "p3": 0}
	removeParticipant(contestParticipants[0])
	assert contestParticipants[0] == {"p1": 0, "p2": 0, "p3": 0}
	add(contestParticipants, constructorScore(13, 20, 8))
	removeParticipant(contestParticipants[2])
	assert contestParticipants[2] == {"p1": 0, "p2": 0, "p3": 0}

def testRemoveParticipantsInterval():
	contestParticipants = []
	add(contestParticipants, constructorScore(1, 2, 3))
	add(contestParticipants, constructorScore(13, 20, 8))
	add(contestParticipants, constructorScore(1, 2, 3))
	add(contestParticipants, constructorScore(13, 20, 8))
	add(contestParticipants, constructorScore(1, 2, 3))
	add(contestParticipants, constructorScore(13, 20, 8))

	removeParticipantsInterval(contestParticipants, 1, 3)
	assert contestParticipants == [{"p1": 1, "p2": 2, "p3": 3}, {"p1": 0, "p2": 0, "p3": 0},
	                               {"p1": 0, "p2": 0, "p3": 0}, {"p1": 0, "p2": 0, "p3": 0},
	                               {"p1": 1, "p2": 2, "p3": 3}, {'p1': 13, 'p2': 20, 'p3': 8}]

def testReplaceScoreOfParticipant():
	contestParticipants = []
	add(contestParticipants, constructorScore(1, 2, 3))
	add(contestParticipants, constructorScore(13, 20, 8))
	add(contestParticipants, constructorScore(1, 2, 3))

	replaceScoreOfParticipant(contestParticipants[1], 8, 'p1')
	assert contestParticipants[1]['p1'] == 8
	replaceScoreOfParticipant(contestParticipants[1], 8, 'p2')
	assert contestParticipants[1]['p2'] == 8
	replaceScoreOfParticipant(contestParticipants[1], 8, 'p3')
	assert contestParticipants[1]['p3'] == 8

	replaceScoreOfParticipant(contestParticipants[2], 4, 'p1')
	assert contestParticipants[2]['p1'] == 4
	replaceScoreOfParticipant(contestParticipants[2], 4, 'p2')
	assert contestParticipants[2]['p2'] == 4
	replaceScoreOfParticipant(contestParticipants[2], 4, 'p3')
	assert contestParticipants[2]['p3'] == 4

def testCalcAverage():
	assert calcAverage(constructorScore(3, 4, 3)) == 3.3333333333333335
	assert calcAverage(constructorScore(3, 3, 3)) == 3
	assert calcAverage(constructorScore(5, 5, 5)) == 5

def testAvg():
	contestParticipants = []
	add(contestParticipants, constructorScore(1, 1, 1))
	add(contestParticipants, constructorScore(1, 1, 1))
	add(contestParticipants, constructorScore(1, 1, 1))
	assert avg(contestParticipants, 0, 2) == 1

def testCalcMinim():
	contestParticipants = []
	add(contestParticipants, constructorScore(1, 2, 3))
	add(contestParticipants, constructorScore(1, 1, 1))
	add(contestParticipants, constructorScore(3, 6, 5))
	assert calcMinim(contestParticipants, 0, 2) == 1

def testUndo():
	contestParticipants = []
	backupParticipants = []

	add(contestParticipants, constructorScore(1, 2, 3))
	x = equals(contestParticipants)
	backupParticipants.append(x)
	add(contestParticipants, constructorScore(1, 1, 1))
	x = equals(contestParticipants)
	backupParticipants.append(x)
	undo(contestParticipants, backupParticipants)
	print(backupParticipants)
	#assert contestParticipants == [{'p1': 1, 'p2': 2, 'p3': 3}]