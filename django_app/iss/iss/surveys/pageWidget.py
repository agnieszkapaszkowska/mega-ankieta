from iss.surveys.abstractWidgetSubclass import AbstractWidgetSubclass


class PageWidget(AbstractWidgetSubclass):
    argsData = {
            'back': {
                'type': 'bool',
                'required': 0,
                'default': 'false'
                },
            }

    unnamedArgs = ['back']
