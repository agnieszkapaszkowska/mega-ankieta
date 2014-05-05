from iss.surveys.abstractParametrisedObject import AbstractParametrisedObject


class Tuple(AbstractParametrisedObject):

    def generate_js(self):
        return 'function() { return ' + self.generate_simple_js() + '}'
