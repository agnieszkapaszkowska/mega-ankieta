from iss.surveys.parser import parseTree
from iss.surveys.survey import Survey


class Arg:
    typeSynonims = {
            "extendedString": ["extendedString", "string", "varId", "structElem"],
            "string": ["string", "varId", "structElem"],
            "number": ["number", "arythmExpr", "varId", "structElem"],
            "bool": ["bool", "varId", "structElem"],
            "listWithTuples": ["listWithTuples", "iterator", "varId", "structElem"],
            "listWithoutTuples": ["listWithoutTuples", "iterator", "varId", "structElem"],
            "tupleWithLists": ["tupleWithLists", "iterator", "varId", "structElem"],
            "tupleWithoutLists": ["tupleWithoutLists", "iterator", "varId", "structElem"],
            "iterator": ["iterator", "varId", "structElem"],
            "datasource": ["datasource", "varId", "structElem"],
            "all": ["string", "extendedString", "varId", "structElem", "number", "arythmExpr", "bool", "iterator", "datasource", "listWithTuples", "listWithoutTuples", "tupleWithLists", "tupleWithoutLists"]
            }

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

        if valueType in self.typeSynonims[self.data['type']]:
            valueTree = self.childrenTrees[-1] # without id if present
            value = Survey.stringToClass(valueType)(valueTree, self.data)
            js = value.getJS() if valueType in ['iterator', 'datasource'] else value.generateJS()

            return ((self.argName + ': ') if self.argName != '' else '') + js

        raise Exception('Argument ' + self.argName + ' should be one of types: ' + \
                str(self.typeSynonims[self.data['type']]) + ' not ' + valueType)
