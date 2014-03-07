from iss.surveys.widget import Widget


class SelectboxWidget(Widget):
    argsData = {
            'name': {
                'type': 'string',
                'required': 1
                },
            'data': {
                'type': 'listWithTuples',
                'required': 1,
                'args': {
                    'type': 'tupleWithoutLists',
                    'args': {
                        'id': {
                            'type': 'string',
                            'required': 1
                            },
                        'text': {
                            'type': 'extendedString',
                            'required': 1
                            }
                        },
                    'unnamedArgs': ['id', 'text'],
                    }
                },
            'selectedIndex': {
                'type': 'number',
                'required': 0,
                'default': '-1'
                }
            }

    unnamedArgs = ['name', 'data', 'selectedIndex']
