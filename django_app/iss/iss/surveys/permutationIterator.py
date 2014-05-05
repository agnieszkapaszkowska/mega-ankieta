from iss.surveys.abstractIteratorSubclass import AbstractIteratorSubclass


class PermutationIterator(AbstractIteratorSubclass):
    args_data = {
        'data': {
            'type': 'listWithTuples',
            'required': 1
        },
    }

    unnamed_args = ['data']
