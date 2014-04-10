from iss.surveys.widget import Widget
from iss.surveys.survey import Survey


class AbstractWidgetSubclass(Widget):

    def generateJS(self):
        simpleJS = self.generateSimpleJS()

        return Survey.surveyVar + ".addWidget(function() {return " + simpleJS + "});"

    def generateSimpleJS(self):
        return 'iss.lib.widgets.Widget("' + self.getWidgetName() +\
               '", ' + Widget.generateSimpleJS(self) + ')'
