from iss.surveys.baseParametrisedObject import BaseParametrisedObject
from iss.surveys.value import Value

class List(BaseParametrisedObject, Value):
    def __init__(self, tree, argsData):
		BaseParametrisedObject.__init__(self, tree[-1])

		self.argsData = argsData
		self.unnamedArgs = []

    def generatePlainJS(self):
        self.createArgs()
        return "array(" + ', '.join(self.jsArgs) + ")"

    def getArgData(self, argName):
        return '', self.argsData['args']

    def checkArg(self, argName):
        pass

    def addArg(self, js, argName):
        self.jsArgs.append(js)

    def checkArgs(self):
        pass

    def completeArgsList(self):
        pass
