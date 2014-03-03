from iss.surveys.survey import Survey
from iss.surveys.parser import parseTree

class StructElem:
    def __init__(self, tree, _ = None):
        self.tree = tree

    def generateJS(self):
        structElem = Survey.text[self.tree[parseTree['START']]:self.tree[parseTree['STOP']]]

        return 'function() { return iss.vars.' + structElem + ' }'
