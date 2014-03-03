from iss.surveys.survey import Survey
from iss.surveys.parser import parseTree

class Bool:
    def __init__(self, tree, _ = None):
        self.tree = tree

    def generateJS(self):
        value = Survey.text[self.tree[parseTree['START']]:self.tree[parseTree['STOP']]]

        return 'function() { return ' + value + ' }'

    def getPythonValue(self):
        return Survey.text[self.tree[parseTree['START']]].lower() == 't'

