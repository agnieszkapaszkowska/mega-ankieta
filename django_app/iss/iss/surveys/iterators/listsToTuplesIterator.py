from iss.surveys.abstractIteratorSubclass import AbstractIteratorSubclass


class ListsToTuplesIterator(AbstractIteratorSubclass):
    args_data = {
        'data': {
            'type': 'tupleWithLists',
            'required': 1
        },
    }

    unnamed_args = ['data']
