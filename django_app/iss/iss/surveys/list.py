from iss.surveys.abstractParametrisedObject import AbstractParametrisedObject
from iss.surveys.parser import parseTree
from iss.surveys.arg import Arg


class List(AbstractParametrisedObject):

    def generateJS(self):
        return 'function() { return ' + self.generateSimpleJS() + '}'

    def generateSimpleJS(self):
        self.createArgs()

        return "[" + ', '.join(self.jsArgsList) + "]"

    def createArgs(self):
        for argTree in self.resultTree[parseTree['CHILDREN_TREES']]:
            js, argName = self.generateArg(argTree)
            self.addToJsArgsList(js, argName)

    def generateArg(self, argTree):
        arg = Arg(argTree)
        arg.setData('', self.argsData)

        return arg.generateJS(), arg.getName()

