from iss.surveys.abstractWidgetSubclass import AbstractWidgetSubclass


class MultipleinputWidget(AbstractWidgetSubclass):
    args_data = {
        'name': {
            'type': 'string',
            'required': 1
        },
        'questions': {
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
                'unnamed_args': ['id', 'text'],
            }
        },
        'answers': {
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
                'unnamed_args': ['id', 'text'],
            }
        },
        'title': {
            'type': 'extendedString',
            'required': 0,
            'default': '""'
        },
        'required': {
            'type': 'bool',
            'required': 0,
            'default': 'true'
        },
    }

    unnamed_args = ['name', 'questions', 'answers', 'title', 'required']
