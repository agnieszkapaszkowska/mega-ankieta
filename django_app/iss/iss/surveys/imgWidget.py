from iss.surveys.abstractWidgetSubclass import AbstractWidgetSubclass


class ImgWidget(AbstractWidgetSubclass):
    argsData = {
        'src': {
            'type': 'string',
            'required': 1
        }
    }

    unnamedArgs = ['src']
