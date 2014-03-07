from iss.surveys.widget import Widget


class PageWidget(Widget):
    argsData = {
            'back': {
                'type': 'bool',
                'required': 0,
                'default': 'false'
                },
            }

    unnamedArgs = ['back']
