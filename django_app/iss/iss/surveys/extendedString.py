from iss.surveys.survey import Survey
from iss.surveys.parser import parseTree
from iss.surveys.value import Value


class ExtendedString(Value):

    def generateJS(self):
        return "function() { with (iss.vars) { return " + self.generateSimpleJS() + '} }'

    def generateSimpleJS(self):
        text = []

        for production in self.resultTree[parseTree['CHILDREN_TREES']]:
            prodClass = Survey.stringToClass(production[parseTree['PROD_NAME']])

            text.append('(' + prodClass(production).generateSimpleJS() + ')')

        return ' + '.join(text)
