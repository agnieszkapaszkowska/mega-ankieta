from iss.surveys.value import Value


class InnerString(Value):

    def generatePlainJS(self):
        return '"' + Value.generateSimpleJS() + '"'
