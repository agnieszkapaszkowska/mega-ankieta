from iss.surveys.baseParametrisedObject import BaseParametrisedObject
from iss.surveys.survey import Survey

class Iterator(BaseParametrisedObject):
    def generateJS(self):
        self.createArgs()

        return 'function () { return iss.lib.iterators.' + self.getClassName() +\
				'({' + ', '.join(self.jsArgs) + '});'
