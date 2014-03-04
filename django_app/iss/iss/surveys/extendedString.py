from iss.surveys.survey import Survey
from iss.surveys.parser import parseTree

class ExtendedString:
	def __init__(self, tree, x = {}):
		self.tree = tree

	def generateJS(self):
		return "function() { with (iss.vars) { return " +\
				self.generatePlainJS() + '; } }'

	def generatePlainJS(self):
		text = ""

		for production in self.tree[parseTree['CHILDREN_TREES']]:
			prodClass = Survey.stringToClass(production[parseTree['PROD_NAME']])

			text += '(' + prodClass(production).generatePlainJS() + ')+\n'

		text += "''"

		return text
