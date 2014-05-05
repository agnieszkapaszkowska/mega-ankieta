from iss.surveys.widget import Widget
from iss.surveys.abstractWidgetSubclass import AbstractWidgetSubclass


class AbstractWidgetContainerSubclass(AbstractWidgetSubclass):

    def generate_simple_js(self):
        return 'iss.lib.widgets.' + self.get_class_name() +\
            '(' + Widget.generate_simple_js(self) + ')'
