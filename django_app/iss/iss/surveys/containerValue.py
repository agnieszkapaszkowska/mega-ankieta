from iss.surveys.baseParametrisedObject import BaseParametrisedObject
from iss.surveys.value import Value


class ContainerValue(BaseParametrisedObject, Value):
    def __init__(self, childrenTrees, argsData=None):
        BaseParametrisedObject.__init__(self, childrenTrees)
        if argsData is None:
            self.argsData = None
        else:
            self.argsData = argsData['args']
            self.unnamedArgs = argsData['unnamedArgs'] if 'unnamedArgs' in argsData else []
    
    def getJS(self):
        return Value.getJS(self)
   
    def createArgs(self):
        if self.argsData is None:
            return self.createArgsWithoutType({'type' : 'all',
                                               'args' : self.argsData})
        return self.createArgsWithType()

    def createArgsWithType(self):
        return BaseParametrisedObject.createArgs(self)
