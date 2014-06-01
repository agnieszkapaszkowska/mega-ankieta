from iss.surveys.abstractWidgetContainerSubclass import AbstractWidgetContainerSubclass


class SurveyWidget(AbstractWidgetContainerSubclass):
    args_data = {
        'name': {
            'type': 'string',
            'required': 0,
            'default': 'undefined'
        },
        'destination': {
            'type': 'string',
            'required': 0,
            'default': 'undefined'
        },
        'container': {
            'type': 'string',
            'required': 0,
            'default': '"#image .panel-body"'
        }
    }

    unnamed_args = ['name', 'destination', 'container']
