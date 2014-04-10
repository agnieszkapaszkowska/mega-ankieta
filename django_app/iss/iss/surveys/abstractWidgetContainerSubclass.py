from iss.surveys.widget import Widget
from iss.surveys.abstractWidgetSubclass import AbstractWidgetSubclass


class AbstractWidgetContainerSubclass(AbstractWidgetSubclass):

    def generateSimpleJS(self):
        return 'iss.lib.widgets.' + self.getClassName() +\
            '(' + Widget.generateSimpleJS(self) + ')'
