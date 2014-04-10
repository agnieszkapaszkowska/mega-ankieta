from iss.surveys.abstractWidgetSubclass import AbstractWidgetSubclass


class TextWidget(AbstractWidgetSubclass):
    argsData = {
        'text': {
            'type': 'extendedString',
            'required': 1
        }
    }

    unnamedArgs = ['text']
