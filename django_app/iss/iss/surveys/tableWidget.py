from iss.surveys.abstractWidgetSubclass import AbstractWidgetSubclass


class TableWidget(AbstractWidgetSubclass):
    argsData = {
        'name': {
            'type': 'string',
            'required': 1
        },
        'data': {
            'type': 'tupleWithLists',
            'required': 1,
            'untypedArgs': {
                'type': 'listWithoutTuples',
            }
        },
        'number': {
            'type': 'number',
            'required': 1
        },
        'required': {
            'type': 'bool',
            'required': 0,
            'default': 'false'
        },
    }

    unnamedArgs = ['name', 'data', 'number', 'required']
