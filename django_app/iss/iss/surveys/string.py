from iss.surveys.value import Value


class String(Value):

    def getPythonValue(self):
        return self.generatePlainJS()[1:-1]
