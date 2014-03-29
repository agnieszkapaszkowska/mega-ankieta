from iss.surveys.abstractIteratorSubclass import AbstractIteratorSubclass


class PermutationIterator(AbstractIteratorSubclass):
    argsData = {
            'data':{
                'type': 'listWithTuples',
                'required': 1
                },
            }

    unnamedArgs = ['data']
