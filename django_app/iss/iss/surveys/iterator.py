from iss.surveys.parametrisedValue import ParametrisedValue


class Iterator(ParametrisedValue):

    def generatePlainJS(self):
        return 'iss.lib.iterators.' + self.getClassName() +\
                '(' + ParametrisedValue.generatePlainJS(self) + ')'

