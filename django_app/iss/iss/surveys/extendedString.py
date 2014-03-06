from iss.surveys.survey import Survey
from iss.surveys.parser import parseTree
from iss.surveys.value import Value

class ExtendedString(Value):
	def generateJS(self):
		return "function() { with (iss.vars) { return " + self.generatePlainJS() + '; } }'

	def generatePlainJS(self):
		text = ""

		for production in self.childrenTrees[parseTree['CHILDREN_TREES']]:
			prodClass = Survey.stringToClass(production[parseTree['PROD_NAME']])

			text += '(' + prodClass(production).generatePlainJS() + ')+\n'

		text += "''"

		return text
