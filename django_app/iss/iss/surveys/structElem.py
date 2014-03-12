from iss.surveys.value import Value


class StructElem(Value):

    def generateJS(self):
        return 'function() { return ' + self.generateSimpleJS() + ' }'

    def generateSimpleJS(self):
        return 'iss.vars.' + Value.generateSimpleJS(self)
