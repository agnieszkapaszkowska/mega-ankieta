from iss.surveys.containerValue import ContainerValue


class Tuple(ContainerValue):
    
    def generatePlainJS(self):
        self.createArgs()
        return "{" + ', '.join(self.jsArgs) + "}"
