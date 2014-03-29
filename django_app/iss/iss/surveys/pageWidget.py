from iss.surveys.abstractWidgetContainerSubclass import AbstractWidgetContainerSubclass


class PageWidget(AbstractWidgetContainerSubclass):
    argsData = {
            'back': {
                'type': 'bool',
                'required': 0,
                'default': 'false'
                },
            'buttons': {
                'type': 'bool',
                'required': 0,
                'default': 'true'
                },
            'nextbuttontext': {
                    'type': 'extendedString',
                    'required': 0,
                    'default': '"Next"'
                },
            'prevbuttontext': {
                    'type': 'extendedString',
                    'required': 0,
                    'default': '"Prev"'
                },
            }

    unnamedArgs = ['back', 'buttons', 'nextbuttontext', 'prevbuttontext']
