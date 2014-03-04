from iss.surveys.survey import Survey
from iss.surveys.parser import parseTree

class Condition:
    def __init__(self, tree, _ = None):
        self.tree = tree

    def generateJS(self):
        return 'function() { with (iss.vars) { return (' + self.generatePlainJS()+ ') }}'

    def generatePlainJS(self):
        return Survey.text[self.tree[parseTree['START']]:self.tree[parseTree['STOP']]]
