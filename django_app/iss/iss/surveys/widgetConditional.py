from iss.surveys.abstractParametrisedObject import AbstractParametrisedObject
from iss.surveys.condition import Condition
from iss.surveys.survey import Survey
from parser import parseTree


class WidgetConditional(AbstractParametrisedObject):

    def generateJS(self):
        first = True
        condition = False
        js = ''
        for component in self.resultTree[parseTree['CHILDREN_TREES']]:
            if component[parseTree['PROD_NAME']] == 'condition':
                condition = True
                if not first:
                    js += "else "
                first = False
                js += "if (" + Condition(
                    component).generateJS() + "() ) {\n"
            else:
                if not condition:
                    js += "else {\n"
                condition = False
                js += Survey.generateProductionsJS(
                    component[parseTree['CHILDREN_TREES']]) + "}\n"
        return (Survey.surveyVar
                + ".addWidgetConditional( function() {"
                + js + "});")
