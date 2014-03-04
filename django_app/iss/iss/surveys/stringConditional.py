from iss.surveys.survey import Survey
from iss.surveys.parser import parseTree

class StringConditional:
    def __init__(self, tree, _ = None):
        self.tree = tree

    def generatePlainJS(self):
		jsParts = []

		for production in self.tree[parseTree['CHILDREN_TREES']]:
			prodClass = Survey.stringToClass(production[parseTree['PROD_NAME']])

			jsParts.append(prodClass(production).generatePlainJS())


		hasElse = len(jsParts) == 3

		return '(' + jsParts[0] + ')?(' + jsParts[1] + '):(' +\
				(jsParts[2] if hasElse else '""') + ')'
