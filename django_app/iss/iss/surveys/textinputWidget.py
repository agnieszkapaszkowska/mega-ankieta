from iss.surveys.widget import Widget

class TextinputWidget(Widget):
	argsData = {
			'name': {
				'type': 'string',
				'required': 1
				},
			'label': {
				'type': 'extendedString',
				'required': 0,
				'default': '""'
				},
			'placeholder': {
				'type': 'extendedString',
				'required': 0,
				'default': '""'
				}
			}

	unnamedArgs = ['name', 'label', 'placeholder']
