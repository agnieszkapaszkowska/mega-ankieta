from iss.surveys.abstractParametrisedObject import AbstractParametrisedObject
from iss.surveys.condition import Condition
from iss.surveys.survey import Survey
from parser import parseTree


class WidgetConditional(AbstractParametrisedObject):

    def generateJS(self):
        condition = ''
        conditions = []
        js = []
        for component in self.resultTree[parseTree['CHILDREN_TREES']]:
            if component[parseTree['PROD_NAME']] == 'condition':
                condition = Condition(
                    component).generateJS()
            else:
                js.append("{condition: function() { return "
                          + condition + "()" + (
                              " && " + " && ".join(conditions)
                              if len(conditions) > 0 else "")
                          + " }, body: function() { "
                          + Survey.generateProductionsJS(
                                component[parseTree['CHILDREN_TREES']])
                          + "}}")
                conditions.append("!(" + condition + "())")
                condition = ''
        return (Survey.surveyVar
                + ".addWidgetConditional([" + ",".join(js) + "]);\n")
