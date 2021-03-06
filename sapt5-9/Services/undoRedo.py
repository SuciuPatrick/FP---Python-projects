class UndoService:
	def __init__(self):
		self._operations = []
		self._index = -1
		self._duringUndo = False

	def addOperation(self, operation):
		if self._duringUndo == True:
			return
		self._index += 1
		self._operations = self._operations[:self._index + 1]
		self._operations.append(operation)

	def undo(self):
		if self._index == -1:
			return False
		self._duringUndo = True
		self._operations[self._index].undo()
		self._duringUndo = False
		self._index -= 1
		return True

	def redo(self):
		if self._index + 1 >= len(self._operations) or (self._index == -1 and len(self._operations) == 0):
			return False
		self._duringUndo = True
		self._index += 1
		self._operations[self._index].redo()
		self._duringUndo = False
		return True

class FunctionCall:
	def __init__(self, func, *params):
		self._func = func
		self._params = params

	def call(self):
		self._func(*self._params)

class Operation:
	def __init__(self, undoFunction, redoFunction):
		self._undoFunction = undoFunction
		self._redoFunction = redoFunction

	def undo(self):
		self._undoFunction.call()

	def redo(self):
		self._redoFunction.call()


class CascadedOperation:
	def __init__(self):
		self._operation = []

	def add(self, oper):
		self._operation.append(oper)

	def undo(self):
		for o in self._operation:
			o.undo()

	def redo(self):
		for o in self._operation:
			o.redo()