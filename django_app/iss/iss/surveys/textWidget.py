from iss.surveys.abstractWidgetSubclass import AbstractWidgetSubclass


class TextWidget(AbstractWidgetSubclass):
    args_data = {
        'text': {
            'type': 'extendedString',
            'required': 1
        }
    }

    unnamed_args = ['text']
