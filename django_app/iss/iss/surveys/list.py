from iss.surveys.containerValue import ContainerValue

class List(ContainerValue):
    
    def generatePlainJS(self):
        self.createArgs()
        return "array(" + ', '.join(self.jsArgs) + ")"

    def getArgData(self, argName):
        if self.argsData is None:
            return '', {'type' : 'all'}
        return '', self.argsData

    def checkArg(self, argName):
        pass

    def addArg(self, js, argName):
        self.jsArgs.append(js)

    def checkArgs(self):
        pass

    def completeArgsList(self):
        pass
