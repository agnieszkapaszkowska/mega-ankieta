from iss.surveys.parser import parseTree
from iss.surveys.survey import Survey


class Arg:
    typeSynonims = {
        "extendedString":   ["extendedString", "string", "varId", "structElem"],
        "string":           ["string", "varId", "structElem"],
        "number":           ["number", "arythmExpr", "varId", "structElem"],
        "bool":             ["condition", "bool", "varId", "structElem"],
        "listWithTuples":   ["listWithTuples", "iterator", "varId", "structElem"],
        "listWithoutTuples": ["listWithoutTuples", "iterator", "varId", "structElem"],
        "tupleWithLists":   ["tupleWithLists", "iterator", "varId", "structElem"],
        "tupleWithoutLists": ["tupleWithoutLists", "iterator", "varId", "structElem"],
        "iterator":         ["iterator", "varId", "structElem"],
        "datasource":       ["datasource", "varId", "structElem"],
    }

    def __init__(self, resultTree):
        childrenTrees = resultTree[parseTree['CHILDREN_TREES']]
        self.valueTree = childrenTrees[-1]

        if len(childrenTrees) == 2:
            start = childrenTrees[0][parseTree['START']]
            stop = childrenTrees[0][parseTree['STOP']]
            self.name = Survey.text[start:stop]
        else:
            self.name = ''

    def setData(self, name, data):
        self.name = name
        self.data = data

    def getName(self):
        return self.name

    def generateJS(self):
        valueType = self.valueTree[parseTree['PROD_NAME']]

        if self.data and not valueType in self.typeSynonims[self.data['type']]:
            raise Exception('Argument ' + self.name + ' should be one of types: ' +
                            str(self.typeSynonims[self.data['type']]) + ' not ' + valueType)

        value = Survey.stringToClass(valueType)(self.valueTree, self.data)
        js = value.generateJS()

        return ((self.name + ': ') if len(self.name) else '') + js
