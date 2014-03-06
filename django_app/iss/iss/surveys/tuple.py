from iss.surveys.parametrisedValue import ParametrisedValue

class Tuple(ParametrisedValue):
    def __init__(self, tree, argsData):
		ParametrisedValue.__init__(self, tree[-1])

		self.argsData = argsData['args']
		self.unnamedArgs = argsData['unnamedArgs']
