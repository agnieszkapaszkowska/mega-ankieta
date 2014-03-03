from iss.surveys.survey import Survey
from iss.surveys.parser import parseTree

class Number:
    def __init__(self, tree, _ = None):
        self.tree = tree

    def generateJS(self):
        num = Survey.text[self.tree[parseTree['START']]:self.tree[parseTree['STOP']]]

        return 'function() { return ' + num + ' }'

    def getPythonValue(self):
        return float(Survey.text[self.tree[parseTree['START']]:self.tree[parseTree['STOP']]])

