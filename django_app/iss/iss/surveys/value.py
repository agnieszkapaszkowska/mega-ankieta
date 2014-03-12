from iss.surveys.survey import Survey
from iss.surveys.parser import parseTree


class Value:

    def __init__(self, resultTree, _ = None):
        self.resultTree = resultTree

    def generateJS(self):
        return 'function() { return ' + self.generateSimpleJS()+ ' }'

    def generateSimpleJS(self):
        start = self.resultTree[parseTree['START']]
        stop = self.resultTree[parseTree['STOP']]

        return Survey.text[start:stop]
