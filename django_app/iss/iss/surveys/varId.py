from iss.surveys.value import Value


class VarId(Value):

    def generateJS(self):
        return 'function() { return iss.vars.' + self.generateSimpleJS() + ' }'

    def generateSimpleJS(self):
        return 'iss.vars.' + Value.generateSimpleJS(self)
