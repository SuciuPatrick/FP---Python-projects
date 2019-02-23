
from ui_functions_menu import ui_add, ui_remove, ui_main, showMenuDrivenList
from ui_functions_command import ui_add_command, ui_remove_command, ui_list_command, printHelp, \
	ui_avg_min_command, ui_podium_command, ui_undo_command
from add_insert import addForTests
from tests import tests
from list import equals

def run():
	listOfParticipants = []
	addForTests(listOfParticipants)
	ui_main()
	value = input('Insert a number from the list: -> ')
	if value == '1':  # Value for menu driven
		while True:
			showMenuDrivenList()  # Afisare meniu de optiuni pentru operatii pe lista
			valueMenu = input('Insert a number for an operation from the list: -> ')
			if valueMenu == '1':  #The case for add and insert
				ui_add(listOfParticipants)
			elif valueMenu == '2':
				ui_remove(listOfParticipants)
			elif valueMenu == 'x' or valueMenu == 'X':  #The case to exit from the app
				return
			elif valueMenu == 'p' or 'P':
				for part in listOfParticipants:
					print(part)

	if value == '2':  #Value for command driven
		backupParticipants = []
		while True:
			valueMenu = input('Insert an operation: -> ')
			parts = valueMenu.split()
			if (parts[0] == 'add' or parts[0] == 'remove' or parts[0] == 'insert' or parts[0] == 'replace'):
				x = equals(listOfParticipants)
				backupParticipants.append(x)
			if parts[0] == 'add' or parts[0] == 'insert':  #The case for add and insert
				ui_add_command(listOfParticipants, parts)
			elif parts[0] == 'remove' or parts[0] == 'replace':
				ui_remove_command(listOfParticipants, parts)
			elif valueMenu == 'x' or valueMenu == 'X':  #The case to exit from the app
				return
			elif  parts[0] == 'list':
				ui_list_command(listOfParticipants, parts)
			elif valueMenu == 'help':
				printHelp()
			elif parts[0] == 'avg' or parts[0] == 'min':
				ui_avg_min_command(listOfParticipants, parts)
			elif parts[0] =='top':
				ui_podium_command(listOfParticipants, parts)
			elif parts[0] == 'undo':
				ui_undo_command(listOfParticipants, parts, backupParticipants)
tests()
run()
