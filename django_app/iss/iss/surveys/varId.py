from iss.surveys.survey import Survey
from iss.surveys.parser import parseTree

class VarId:
    def __init__(self, tree, _ = None):
        self.tree = tree

    def generateJS(self):
        varId = Survey.text[self.tree[parseTree['START']]:self.tree[parseTree['STOP']]]

        return 'function() { return iss.vars.' + varId + ' }'
