from iss.surveys.survey import Survey
from iss.surveys.parser import parseTree

class ArythmExpr:
    def __init__(self, tree, _ = None):
        self.tree = tree

    def generateJS(self):
        expr = Survey.text[self.tree[parseTree['START']]:self.tree[parseTree['STOP']]]

        return 'function() { with (iss.vars) { return ' + expr + ' }}'
