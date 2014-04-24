from iss.surveys.widget import Widget
from iss.surveys.survey import Survey


class AbstractWidgetSubclass(Widget):

    def generate_js(self):
        simple_js = self.generate_simple_js()

        return Survey.survey_var + ".addWidget(function() {return " + simple_js + "});"

    def generate_simple_js(self):
        return 'iss.lib.widgets.Widget("' + self.get_widget_name() +\
               '", ' + Widget.generate_simple_js(self) + ')'
