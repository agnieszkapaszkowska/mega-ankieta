from iss.surveys.survey import Survey
from iss.surveys.parser import parseTree
from iss.surveys.value import Value


class StringConditional(Value):

    def generateSimpleJS(self):
        jsParts = []

        for production in self.resultTree[parseTree['CHILDREN_TREES']]:
            prodClass = Survey.stringToClass(production[parseTree['PROD_NAME']])

            jsParts.append(prodClass(production).generateSimpleJS())
            

        hasElse = len(jsParts) == 3

        return '((' + jsParts[0] + ')?(' + jsParts[1] + '):(' +\
                (jsParts[2] if hasElse else '""') + '))'
