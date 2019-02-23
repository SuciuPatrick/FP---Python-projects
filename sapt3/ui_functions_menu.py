from add_insert import constructorScore, add, insert
from remove import removeParticipant, removeParticipantsInterval, replaceScoreOfParticipant


def ui_main():
	print("\t1. Menu interface")
	print("\t2. Command interface")

def showMenuDrivenList():
	print("\t1. Add the result of a new participant.")
	print("\t2. Modify the scores from the list")
	print("\t3. Write the participants whose score has different properties.")
	print("\tP. Press P to print the list")
	print("\tPress x or X to exit")

# Tratam cazurile pentru add si insert
def ui_add(listOfParticipants):
	print('\t1. Add participant and his scores')
	print('\t2. Insert participant and his position')
	valueAdd = input('Insert a number for the list: -> ')
	if valueAdd == '1':  #add, we treat the case that we add at the end of the list
		while True:
			try:
				P1 = int(input('P1-> '))
				P2 = int(input('P2-> '))
				P3 = int(input('P3-> '))
				if P1 < 0 or P2 < 0 or P3 < 0:
					print("A score can't be negative. Please try again and insert a positive number.")
				else:
					add(listOfParticipants, constructorScore(P1, P2, P3))
				break
			except ValueError:
				print("Insert an integer, please!")
	elif valueAdd == '2':  #the case where we set the position, if is out of range-> error
		while True:
			try:
				P1 = int(input('P1-> '))
				P2 = int(input('P2-> '))
				P3 = int(input('P3-> '))
				position = int(input('insert position-> '))
				n = len(listOfParticipants)
				if n < position:
					print("Invalid position because is out of range. ")
				else:
					insert(listOfParticipants, constructorScore(P1, P2, P3), position)
					break
			except ValueError:
				print('Insert an integer, please!')
	else:
		print("Sorry but your input is invalid. Please insert a value from the list.")

def ui_remove(listOfParticipants):
	print('\t1. Remove position. Set the scores at this position to 0')
	print('\t2. Remove position - to position. Set the scores at this positions to 0')
	print('\t3. Replace the scores for a position with new one(Insert P1, P2, P3)')
	valueRemove = input('Insert a number for the list: -> ')
	if valueRemove == '1':
		while True:
			try:
				value = int(input('Position to remove -> '))
				if value < 0 or value > len(listOfParticipants):
					print("Insert a valid position")
				removeParticipant(listOfParticipants[value])
				break
			except ValueError:
				print("Insert an integer")
	elif valueRemove == '2':
		while True:
			try:
				start = int(input('start-> '))
				end = int(input('end-> '))
				removeParticipantsInterval(listOfParticipants, start, end)
				break
			except ValueError:
				print("Insert a valid integer, please!")
	elif valueRemove == '3':
		while True:
			try:
				position = int(input("insert the position-> "))
				grade = input("insert the grade you want to be modify: ex p1, p2, p3-> ")
				newScore = int(input("insert the new score-> "))
				if 0 <= newScore <= 10:
					if replaceScoreOfParticipant(listOfParticipants[position], newScore, grade) is False:
						print("invalid grade syntax, please check the examples!")
					else:
						break
				else:
					print("Invalid newScore. The grade must be between 0 and 10.")
			except ValueError:
				print("Invalid syntax, please try again")
	else:
		print("Sorry but your input is invalid. Please insert a value from the list.")
