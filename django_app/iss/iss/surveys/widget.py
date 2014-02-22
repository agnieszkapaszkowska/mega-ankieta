from iss.surveys.baseParametrisedObject import BaseParametrisedObject
from iss.surveys.survey import Survey

class Widget(BaseParametrisedObject):
    def generateJS(self):
        self.createArgs()

        return Survey.surveyVar + ".addWidget('" + self.getClassName() +\
                "', {" + ', '.join(self.jsArgs) + "});"
