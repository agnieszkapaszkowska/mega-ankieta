from iss.surveys.value import Value

class StructElem(Value):
    def generateJS(self):
        return 'function() { return iss.vars.' + self.generatePlainJS() + ' }'
