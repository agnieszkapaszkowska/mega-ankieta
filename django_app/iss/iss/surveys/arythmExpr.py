from iss.surveys.value import Value


class ArythmExpr(Value):

    def generateJS(self):
        return 'function() { with (iss.vars) { return (' + self.generatePlainJS() + ') }}'
