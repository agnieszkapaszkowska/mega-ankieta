from iss.surveys.abstractWidgetSubclass import AbstractWidgetSubclass


class LikertWidget(AbstractWidgetSubclass):
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
            'answers': {
                'type': 'listWithTuples',
                'required': 0,
                'default': '[function() { return "1" }, function() { return "2" }, function() { return "3" }, function() { return "4" }, function() { return "5" }]'
                },
            'required': {
                    'type': 'bool',
                    'required': 0,
                    'default': 'false'
                },
			}

	unnamedArgs = ['name', 'data', 'answers', 'required']
