from iss.surveys.widget import Widget


class CheckboxWidget(Widget):
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
			}

	unnamedArgs = ['name', 'data']
