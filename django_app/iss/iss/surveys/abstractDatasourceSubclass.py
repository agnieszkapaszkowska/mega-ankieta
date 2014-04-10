from iss.surveys.datasource import Datasource
from iss.surveys.survey import Survey


class AbstractDatasourceSubclass(Datasource):

    def generateJS(self):
        simpleJS = self.generateSimpleJS()

        return "function() {return " + simpleJS + "}"

    def generateSimpleJS(self):
        return 'iss.lib.datasources.' + self.getClassName() +\
            '(' + Datasource.generateSimpleJS(self) + ')'
