from iss.surveys.baseParametrisedObject import BaseParametrisedObject
from iss.surveys.survey import Survey
from iss.surveys.varId import VarId

class AssignmentLeft(BaseParametrisedObject):
    def getJS(self):
        prodName, _, _, _ = self.childrenTrees[1]
        production = Survey.stringToClass(prodName)(self.childrenTrees[1])
        js = production.getJS()
        varId = VarId(self.childrenTrees[0])
        return '\n' + 'var var.iss.' + varId.generatePlainJS() + ' = ' + js
