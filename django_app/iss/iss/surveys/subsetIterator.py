from iss.surveys.abstractIteratorSubclass import AbstractIteratorSubclass


class SubsetIterator(AbstractIteratorSubclass):
    args_data = {
        'data': {
            'type': 'listWithTuples',
            'required': 1
        },
        'number': {
            'type': 'number',
            'required': 1
        },
    }

    unnamed_args = ['data', 'number']
