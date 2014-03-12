from iss.surveys.abstractWidgetSubclass import AbstractWidgetSubclass


class TextareaWidget(AbstractWidgetSubclass):
    argsData = {
            'name': {
                'type': 'string',
                'required': 1
                },
            'label': {
                'type': 'extendedString',
                'required': 0,
                'default': '""'
                },
            'placeholder': {
                'type': 'extendedString',
                'required': 0,
                'default': '""'
                }
            }

    unnamedArgs = ['name', 'label', 'placeholder']
