from iss.surveys.value import Value

class Condition(Value):
    def generateJS(self):
        return 'function() { with (iss.vars) { return (' + self.generatePlainJS()+ ') }}'
