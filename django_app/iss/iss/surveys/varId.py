from iss.surveys.value import Value


class VarId(Value):

    def generateJS(self):
        return 'function() { return iss.vars.' + self.generatePlainJS() + ' }'

    def generateIdName(self):
        return 'iss.vars.' + self.generatePlainJS()
