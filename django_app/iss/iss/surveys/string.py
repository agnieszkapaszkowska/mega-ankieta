from iss.surveys.value import Value


class String(Value):

    def getPythonValue(self):
        return self.generateSimpleJS()[1:-1]
