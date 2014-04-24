from iss.surveys.abstractParametrisedObject import AbstractParametrisedObject
from iss.surveys.survey import Survey


class Widget(AbstractParametrisedObject):

    def get_widget_name(self):
        class_name = self.get_class_name()
        if len(class_name) == 0:
            return class_name
        return class_name[0].lower() + class_name[1:-6]
