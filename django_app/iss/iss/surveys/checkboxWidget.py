from iss.surveys.abstractWidgetSubclass import AbstractWidgetSubclass


class CheckboxWidget(AbstractWidgetSubclass):
    args_data = {
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
                        },
                        'checked': {
                            'type': 'bool',
                            'required': 0,
                            'default': 'false'
                        }
                    },
                'unnamedArgs': ['id', 'text', 'checked'],
            }
        },
        'horizontal': {
            'type': 'bool',
            'required': 0,
            'default': 'false'
        },
        'required': {
            'type': 'bool',
            'required': 0,
            'default': 'false'
        },
    }

    unnamed_args = ['name', 'data', 'horizontal', 'required']
