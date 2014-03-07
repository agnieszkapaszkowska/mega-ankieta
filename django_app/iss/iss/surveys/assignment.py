from iss.surveys.baseParametrisedObject import BaseParametrisedObject
from iss.surveys.survey import Survey
from iss.surveys.varId import VarId


class Assignment(BaseParametrisedObject):
    def getJS(self):
        return self.getAssignmentVarJS() + ' = ' + self.getAssignmentValueJS()
    
    def getAssignmentVarJS(self):
        varId = VarId(self.childrenTrees[self.varIndex])
        return varId.generateIdName()
        
    def getAssignmentValueJS(self):
        prodName = self.childrenTrees[self.valueIndex][0]
        production = Survey.stringToClass(prodName)(self.childrenTrees[self.valueIndex])
        '''
        if prodName == "widget" production.getJS() 
        returns "iss.survey.addWidget(...)" -> 
            function addWidget in js needs to return function
            returning appropriate parameter to assign on var
        '''
        return production.getJS()

