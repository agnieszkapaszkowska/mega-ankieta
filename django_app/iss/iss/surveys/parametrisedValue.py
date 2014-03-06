from iss.surveys.baseParametrisedObject import BaseParametrisedObject
from iss.surveys.value import Value

class ParametrisedValue(BaseParametrisedObject, Value):
	def generatePlainJS(self):
		return "{" + ', '.join(self.jsArgs) + "}"
