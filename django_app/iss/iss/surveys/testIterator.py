from iss.surveys.abstractIteratorSubclass import AbstractIteratorSubclass


class TestIterator(AbstractIteratorSubclass):
    args_data = {
        'name': {
            'type': 'datasource',
            'required': 1
        },
    }

    unnamed_args = ['name']
