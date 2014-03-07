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
        return self.generateJS()
    
    def getArgData(self, name):
        if self.argsData is None:
            return name, {'type' : 'all'}
        return super(BasedParametrisedObject, self).getArgData(name)

