from iss.surveys.parser import parseTree
from iss.surveys.survey import Survey

class Arg:
    def __init__(self, childrenTrees):
        self.childrenTrees = childrenTrees

        if childrenTrees[0][parseTree['PROD_NAME']] == 'id':
            start = childrenTrees[0][parseTree['START']]
            stop = childrenTrees[0][parseTree['STOP']]
            self.data = {'name': Survey.text[start:stop]}
        else:
            self.data = {'name': ''}

    def setData(self, data):
        self.data = data

    def getName(self):
        return self.data['name']

    def generateJS(self):
        valueType = self.childrenTrees[-1][parseTree['PROD_NAME']]
        if valueType != self.data['type']:
            raise Exception('Argument ' + self.data['name'] + ' should be of type ' + \
                    self.data['type'] + ' not ' + valueType)

        value = Survey.stringToClass(valueType)

        return self.data['name'] + ': ' + value(self.childrenTrees[-1]).generateJS()
