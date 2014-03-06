from iss.surveys.survey import Survey
from iss.surveys.parser import parseTree

class Value:
    def __init__(self, childrenTrees, _ = None):
        self.childrenTrees = childrenTrees

    def generateJS(self):
        return 'function() { return ' + self.generatePlainJS()+ ' }'

    def generatePlainJS(self):
		start = self.childrenTrees[parseTree['START']]
		stop = self.childrenTrees[parseTree['STOP']]

		return Survey.text[start:stop]
