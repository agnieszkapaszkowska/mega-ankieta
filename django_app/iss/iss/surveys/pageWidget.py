from iss.surveys.widget import Widget

class PageWidget(Widget):
	argsData = {
			'id': {
				'type': 'string',
				'required': 1
				},
			'back': {
				'type': 'bool',
				'required': 0,
				'default': 'false'
				},
			'id': {
				'type': 'string',
				'required': 1
				},
			'id': {
				'type': 'string',
				'required': 1
				},
			}

	unnamedArgs = ['name', 'data', 'checkedIndex']
