from iss.surveys.arg import Arg
from iss.surveys.string import String
from iss.surveys.survey import Survey


class BaseParametrisedObject:

    def __init__(self, childrenTrees, _ = None):
        self.childrenTrees = childrenTrees[-1]
        self.foundUnnamedArgs = 0
        self.foundArgs = {}
        self.jsArgs = []
        self.name = ''

    def getName(self):
        return self.name

    def createArgs(self):
        for _, _, _, argTree in self.childrenTrees:
            js, argName = self.getArg(argTree)
            self.checkArg(argName)
            self.addArg(js, argName)

        self.checkArgs()
        self.completeArgsList()

    def createArgsWithoutType(self, argsData):
        for _, _, _, argTree in self.childrenTrees:
            arg = Arg(argTree)
            arg.setData(arg.getName(), argsData)
            self.jsArgs.append(arg.generateJS())

    def getArg(self,argTree):
        arg = Arg(argTree)
        arg.setData(*self.getArgData(arg.getName()))
        return arg.generateJS(), arg.getName()

    def getArgData(self, argName):
        if len(argName) == 0:
            if len(self.unnamedArgs) == self.foundUnnamedArgs:
                raise Exception(self.getClassName() +\
                        " accepts only " + str(len(self.unnamedArgs)) +\
                        " unnamed arguments")

            argName = self.unnamedArgs[self.foundUnnamedArgs]

        if argName in self.argsData:
            return argName, self.argsData[argName]

        raise Exception(self.getClassName() +\
                " does not accept parameter named " + argName)

    def addArg(self, js, argName):
        self.foundArgs[argName] = 1

        if argName == self.unnamedArgs[self.foundUnnamedArgs]:
            while True:
                self.foundUnnamedArgs += 1

                if len(self.unnamedArgs) == self.foundUnnamedArgs or\
                        not self.unnamedArgs[self.foundUnnamedArgs] in self.foundArgs:
                            break

        self.jsArgs.append(js)

    def checkArg(self, argName):
        if argName in self.foundArgs:
            raise Exception("You cannot use two same-named arguments in one parametrised object")

    def checkArgs(self):
        for name in self.argsData:
            if self.argsData[name]['required'] and not name in self.foundArgs:
                raise Exception('Required argument "' + name + '" wasn\'t supplied')

    def completeArgsList(self):
        for name in self.argsData:
            if not self.argsData[name]['required'] and not name in self.foundArgs:
                self.jsArgs.append(name + ": function() { return " + self.argsData[name]['default'] + " }")

    def getClassName(self):
        return self.__class__.__name__

    def getJS(self):
        specialisedClass = self.getSpecialisedClass(self.childrenTrees[0], self.getClassName())
        return specialisedClass([self.childrenTrees[1:]]).generateJS()

    def getSpecialisedClass(self, stringTree, baseClassName):
        subclassName = String(stringTree).getPythonValue()

        return Survey.stringToClass(subclassName + baseClassName)
