from iss.surveys.abstractIteratorSubclass import AbstractIteratorSubclass


class ListsToTuplesIterator(AbstractIteratorSubclass):
    argsData = {
        'data': {
            'type': 'tupleWithLists',
            'required': 1
        },
    }

    unnamedArgs = ['data']
