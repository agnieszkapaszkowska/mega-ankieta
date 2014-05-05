from iss.surveys.abstractWidgetSubclass import AbstractWidgetSubclass


class ImgWidget(AbstractWidgetSubclass):
    args_data = {
        'src': {
            'type': 'string',
            'required': 1
        }
    }

    unnamed_args = ['src']
