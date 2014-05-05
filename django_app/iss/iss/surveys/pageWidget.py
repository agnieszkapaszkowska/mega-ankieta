from iss.surveys.abstractWidgetContainerSubclass import AbstractWidgetContainerSubclass


class PageWidget(AbstractWidgetContainerSubclass):
    args_data = {
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

    unnamed_args = ['back', 'buttons', 'nextbuttontext', 'prevbuttontext']
