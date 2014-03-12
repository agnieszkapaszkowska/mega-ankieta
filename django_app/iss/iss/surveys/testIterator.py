from iss.surveys.abstractIteratorSubclass import AbstractIteratorSubclass


class TestIterator(AbstractIteratorSubclass):
    argsData = {
            'name':{
                'type': 'datasource',
                'required': 1
                },
            }

    unnamedArgs = ['name']
