from iss.surveys.iterator import Iterator
from iss.surveys.survey import Survey


class AbstractIteratorSubclass(Iterator):

    def generateJS(self):
        simpleJS = self.generateSimpleJS()

        return "function() {return " + simpleJS + "}"

    def generateSimpleJS(self):
        return 'iss.lib.iterators.' + self.getClassName() +\
            '(' + Iterator.generateSimpleJS(self) + ')'
