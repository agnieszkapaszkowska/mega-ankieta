from iss.surveys.containerValue import ContainerValue


class List(ContainerValue):
    
    def generatePlainJS(self):
        self.createArgs()
        return "array(" + ', '.join(self.jsArgs) + ")"

    def createArgsWithType(self):
        return self.createArgsWithoutType(self.argsData)
