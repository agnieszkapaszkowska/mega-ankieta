from iss.surveys.abstractWidgetSubclass import AbstractWidgetSubclass


class TableWidget(AbstractWidgetSubclass):
    args_data = {
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

    unnamed_args = ['name', 'data', 'number', 'required']
