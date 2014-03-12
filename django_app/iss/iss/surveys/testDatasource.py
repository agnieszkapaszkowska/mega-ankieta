from iss.surveys.abstractDatasourceSubclass import AbstractDatasourceSubclass


class TestDatasource(AbstractDatasourceSubclass):
    argsData = {
            'name':{
                'type': 'string',
                'required': 1
                },
            }

    unnamedArgs = ['name']
