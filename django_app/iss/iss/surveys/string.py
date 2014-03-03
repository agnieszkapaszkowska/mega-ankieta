from iss.surveys.survey import Survey
from iss.surveys.parser import parseTree

class String:
    def __init__(self, tree, x = {}):
        self.tree = tree

    def generateJS(self):
        text = Survey.text[self.tree[parseTree['START']]:self.tree[parseTree['STOP']]]

        return 'function() { return ' + text + ' }'

    def getPythonValue(self):
        return Survey.text[self.tree[parseTree['START']]+1:self.tree[parseTree['STOP']]-1]

