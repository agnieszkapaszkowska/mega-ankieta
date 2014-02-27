from iss.surveys.widget import Widget

class TextWidget(Widget):
	argsData = {
			'text': {
				'type': 'extendedString',
				'required': 1
				}
			}

	unnamedArgs = ['text']
