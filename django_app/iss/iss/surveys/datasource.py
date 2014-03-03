from iss.surveys.baseParametrisedObject import BaseParametrisedObject
from iss.surveys.survey import Survey

class Datasource(BaseParametrisedObject):
    def generateJS(self):
        self.createArgs()

        return 'function () { return iss.lib.datasources.' + self.getClassName() +\
				'({' + ', '.join(self.jsArgs) + '});'
