from iss.surveys.datasource import Datasource


class TestDatasource(Datasource):
    argsData = {
            'name':{
                'type': 'string',
                'required': 1
                },
            }

    unnamedArgs = ['name']
