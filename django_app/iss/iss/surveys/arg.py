from iss.surveys.parser import parseTree
from iss.surveys.survey import Survey

class Arg:
	def __init__(self, childrenTrees):
		self.childrenTrees = childrenTrees

		if childrenTrees[0][parseTree['PROD_NAME']] == 'id':
			start = childrenTrees[0][parseTree['START']]
			stop = childrenTrees[0][parseTree['STOP']]
			self.argName = Survey.text[start:stop]
		else:
			self.argName = ''

	def setData(self, argName, data):
		self.argName = argName
		self.data = data

	def getName(self):
		return self.argName

	def generateJS(self):
		valueType = self.childrenTrees[-1][parseTree['PROD_NAME']]

		for typeVariant in self.data:
			if valueType == typeVariant['type']:
				value = Survey.stringToClass(valueType)(self.childrenTrees[-1], typeVariant)
				js = value.getJS() if valueType in ['iterator', 'datasource'] else value.generateJS()

				return self.argName + ': ' + js

		possibleTypes = map(lambda x: x['type'], self.data)

		raise Exception('Argument ' + self.argName + ' should be one of types: ' + \
				str(possibleTypes) + ' not ' + valueType)
