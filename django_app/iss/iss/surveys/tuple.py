from iss.surveys.abstractParametrisedObject import AbstractParametrisedObject


class Tuple(AbstractParametrisedObject):

    def generateJS(self):
        return 'function() { return ' + self.generateSimpleJS() + '}'
