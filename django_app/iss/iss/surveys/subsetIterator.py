from iss.surveys.abstractIteratorSubclass import AbstractIteratorSubclass


class SubsetIterator(AbstractIteratorSubclass):
    argsData = {
            'data':{
                'type': 'listWithTuples',
                'required': 1
                },
            'number': {
                'type': 'number',
                'required': 1
                },
            }

    unnamedArgs = ['data', 'number']
