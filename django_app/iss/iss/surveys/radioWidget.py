from iss.surveys.abstractWidgetSubclass import AbstractWidgetSubclass


class RadioWidget(AbstractWidgetSubclass):
    argsData = {
            'name':{
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
            'checkedIndex': {
                'type': 'number',
                'required': 0,
                'default': '-1'
                },
            'horizontal': {
                    'type': 'bool',
                    'required': 0,
                    'default': 'false'
                },
            'required': {
                    'type': 'bool',
                    'required': 0,
                    'default': 'true'
                },
            }

    unnamedArgs = ['name', 'data', 'checkedIndex',
                   'horizontal', 'required']
