from iss.surveys.parametrisedValue import ParametrisedValue

class Tuple(ParametrisedValue):
    def __init__(self, tree, argsData):
		super(ParametrisedValue, self).__init__(tree)

		self.argsData = argsData['args']
		self.unnamedArgs = argsData['unnamedArgs']
