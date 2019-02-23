from add_insert import constructorScore, add, insert
from remove import removeParticipant, removeParticipantsInterval, replaceScoreOfParticipant
from list import listCompare, sortList
from avg_min import avg, calcMinim
from podium import sortListP
from undo import undo


def printHelp():
	print("\tadd <P1 score> <P2 score> <P3 score>")
	print("\tinsert <P1 score> <P2 score> <P3 score> at <position>")
	print("\tremove <position>")
	print("\tremove <start position> to <end position>")
	print("\treplace <old score> <P1 | P2 | P3> with <new score>")
	print("\tlist")


def ui_add_command(listOfParticipants, parts):
	if parts[0] == 'add':
		try:
			if len(parts) != 4:
				print("Invalid syntax. Try again!")
			else:
				P1 = int(parts[1])
				P2 = int(parts[2])
				P3 = int(parts[3])

				if P1 >= 0 or P2 >= 0 or P3 >= 0:
					add(listOfParticipants, constructorScore(P1, P2, P3))
				else:
					print("The scores must be positive. Please Try again")
		except ValueError:
			print("Insert an integer, please!")
	elif parts[0] == 'insert':
		if len(parts) != 6:
			print("Invalid syntax. Try again!")
		else:
			try:
				P1 = int(parts[1])
				P2 = int(parts[2])
				P3 = int(parts[3])
				position = int(parts[5])

				if P1 >= 0 or P2 >= 0 or P3 >= 0:
					insert(listOfParticipants, constructorScore(P1, P2, P3), position)
				else:
					print("The scores must be positive. Please Try again")
			except ValueError:
				print("Insert an integer, please!")


def ui_remove_command(listOfParticipants, parts):
	if len(parts) == 2:
		try:
			if int(parts[1]) < 0 or int(parts[1]) > len(listOfParticipants):
				print("Insert a valid position")
				return
			removeParticipant(listOfParticipants[int(parts[1])])
		except ValueError:
			print("Insert an integer")
	elif len(parts) == 4:
		try:
			start = int(parts[1])
			end = int(parts[3])
			removeParticipantsInterval(listOfParticipants, start, end)
		except ValueError:
			print("Insert integers.")
	elif len(parts) == 5:
		try:
			position = int(parts[1])
			grade = parts[2]
			newScore = int(parts[4])
			if 0 <= newScore <= 10:
				if replaceScoreOfParticipant(listOfParticipants[position], newScore, grade) is False:
					print("invalid grade syntax, please check the examples!")
			else:
				print("Invalid newScore. The grade must be between 0 and 10.")
		except ValueError:
			print("Invalid syntax, please try again")


def ui_list_command(listOfParticipants, parts):
	if len(parts) == 1 and parts[0] == 'list':
		for part in listOfParticipants:
			print(part['p1'], part['p2'], part['p3'])
	elif len(parts) == 3:
		try:
			value = int(parts[2])
			sign = parts[1]
			listCompare(listOfParticipants, sign, value)
		except ValueError:
			print("Invalid syntax.")
	elif len(parts) == 2:
		auxParticipants = sortList(listOfParticipants)
		for part in auxParticipants:
			print(part['p1'], part['p2'], part['p3'])


def ui_avg_min_command(listOfParticipants, parts):
	if len(parts) == 4 and parts[0] == 'avg':
		print(avg(listOfParticipants, int(parts[1]), int(parts[3])))
	if len(parts) == 4 and parts[0] == 'min':
		print(calcMinim(listOfParticipants, int(parts[1]), int(parts[3])))


def ui_podium_command(listOfParticipants, parts):
	if len(parts) == 2 and parts[0] == 'top':
		x = sortList(listOfParticipants)
		index = 0
		while index < int(parts[1]):
			print(x[index]['p1'], x[index]['p2'], x[index]['p3'])
			index += 1
	elif len(parts) == 3 and parts[0] == 'top':
		x = sortListP(listOfParticipants, parts[2])
		index = 0
		while index < int(parts[1]):
			print(x[index]['p1'], x[index]['p2'], x[index]['p3'])
			index += 1

def ui_undo_command(listOfParticipants, parts, backupParticipants):
	if parts[0] == 'undo' and len(parts) == 1:
		undo(listOfParticipants, backupParticipants)
