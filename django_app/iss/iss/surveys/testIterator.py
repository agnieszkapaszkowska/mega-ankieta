from iss.surveys.iterator import Iterator


class TestIterator(Iterator):
    argsData = {
            'name':{
                'type': 'datasource',
                'required': 1
                },
            }

    unnamedArgs = ['name']
