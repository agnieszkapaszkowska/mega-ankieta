from iss.surveys.arg import Arg
from iss.surveys.string import String
from iss.surveys.survey import Survey
from iss.surveys.parser import parseTree


class AbstractParametrisedObject:

    argsData = None
    def __init__(self, resultTree, argsData = None, **kwargs):
        self.resultTree = resultTree

        self.foundUnnamedArgs = 0
        self.foundArgsNames = []
        self.jsArgsList = []
        
        if 'additionalJsArgs' in kwargs:
            self.jsArgsList = kwargs['additionalJsArgs']
       
        if not argsData:
            argsData = self.argsData
            if not argsData:
                return

        if 'args' in argsData:
            self.argsData = argsData['args']

        if 'unnamedArgs' in argsData:
            self.unnamedArgs = argsData['unnamedArgs']


    def generateJS(self):
        stringTree = self.resultTree[parseTree['CHILDREN_TREES']][0]
        self.resultTree[parseTree['CHILDREN_TREES']].pop(0)

        widgetSubclass = Survey.stringTreeToClass(stringTree, self.getClassName())
        return widgetSubclass(self.resultTree, additionalJsArgs = self.jsArgsList).generateJS()

    def generateSimpleJS(self):
        self.createArgs()

        return '{' + ', '.join(self.jsArgsList) + '}'

    def createArgs(self):
        if self.argsData:
            self.createTypedArgs()
        else:
            self.createUntypedArgs()

    def createTypedArgs(self):
        for argTree in self.resultTree[parseTree['CHILDREN_TREES']]:
            js, argName = self.generateArg(argTree)
            self.checkArg(argName)
            self.addToJsArgsList(js, argName)

        self.checkArgs()
        self.addDefaultsToJsArgsList()

    def createUntypedArgs(self):
        for argTree in self.resultTree[parseTree['CHILDREN_TREES']]:
            js, argName = self.generateArg(argTree)
            self.addToJsArgsList(js, argName)

    def generateArg(self, argTree):
        arg = Arg(argTree)
        arg.setData(*self.getArgData(arg.getName()))

        return arg.generateJS(), arg.getName()

    def getArgData(self, argName):
        if not self.argsData:
            return argName, None

        if not len(argName):
            if len(self.unnamedArgs) == self.foundUnnamedArgs:
                raise Exception(self.getClassName() +\
                        " accepts only " + str(len(self.unnamedArgs)) +\
                        " unnamed arguments")

            argName = self.unnamedArgs[self.foundUnnamedArgs]

        if argName in self.argsData:
            return argName, self.argsData[argName]

        raise Exception(self.getClassName() +\
                " does not accept parameter named " + argName)

    def addToJsArgsList(self, js, argName):
        if len(argName):
            self.foundArgsNames.append(argName)

            if (hasattr(self, 'unnamedArgs')
                    and argName == self.unnamedArgs[self.foundUnnamedArgs]):
                self.foundUnnamedArgs = self.getNextUnnamedArgIndex()

        self.jsArgsList.append(js)

    def getNextUnnamedArgIndex(self):
        nextIndex = self.foundUnnamedArgs + 1

        while nextIndex != len(self.unnamedArgs) and\
                self.unnamedArgs[nextIndex] in self.foundArgsNames:
            nextIndex += 1

        return nextIndex

    def checkArg(self, argName):
        if argName in self.foundArgsNames:
            raise Exception("You cannot use two same-named arguments in one parametrised object")

    def checkArgs(self):
        for name in self.argsData:
            if self.argsData[name]['required'] and not name in self.foundArgsNames:
                raise Exception('Required argument "' + name + '" wasn\'t supplied')

    def addDefaultsToJsArgsList(self):
        for name in self.argsData:
            if not self.argsData[name]['required'] and not name in self.foundArgsNames:
                self.jsArgsList.append(name + ": function() { return " + self.argsData[name]['default'] + " }")

    def getClassName(self):
        return self.__class__.__name__
'''
    def getJS(self):
        specialisedClass = self.getSpecialisedClass(self.childrenTrees[0], self.getClassName())
        return specialisedClass([self.childrenTrees[1:]]).generateJS()

    def getSpecialisedClass(self, stringTree, baseClassName):
        subclassName = String(stringTree).getPythonValue()

        return Survey.stringToClass(subclassName + baseClassName)
'''
