from iss.surveys.abstractParametrisedObject import AbstractParametrisedObject
from iss.surveys.survey import Survey
from iss.surveys.parser import parseTree
from iss.surveys.varId import VarId
from iss.surveys.value import Value


class Assignment(AbstractParametrisedObject):

    def generateJS(self):
        valueTree = self.resultTree[
            parseTree['CHILDREN_TREES']][self.valueIndex]
        if valueTree[parseTree['PROD_NAME']] == 'widget':
            return self.getWidgetValueJS()

        varJS = self.getAssignmentVarJS()
        valueJS = self.getAssignmentValueJS()

        return Survey.surveyVar + ".addAssignment( function() {" + varJS + ' = ' + valueJS + '() });\n'

    def getAssignmentVarJS(self):
        varTree = self.resultTree[parseTree['CHILDREN_TREES']][self.varIndex]
        varId = VarId(varTree)

        return varId.generateSimpleJS()

    def getAssignmentValueJS(self):
        valueTree = self.resultTree[
            parseTree['CHILDREN_TREES']][self.valueIndex]
        prodName = valueTree[parseTree['PROD_NAME']]
        production = Survey.stringToClass(prodName)(valueTree)

        return production.generateJS()

    def getWidgetValueJS(self):
        childrenTrees = self.resultTree[parseTree['CHILDREN_TREES']]

        valueTree = childrenTrees[self.valueIndex]
        varTree = childrenTrees[self.varIndex]

        varId = Value(varTree).generateSimpleJS()
        widget = Survey.stringToClass('widget')(valueTree,
                                                additionalJsArgs=['resultVarName: "' + varId + '"'])

        return widget.generateJS()
