from iss.surveys.parametrisedValue import ParametrisedValue


class Datasource(ParametrisedValue):

    def generatePlainJS(self):
        return 'iss.lib.datasource.' + self.getClassName() +\
                '(' + ParametrisedValue.generatePlainJS(self) + ')'


