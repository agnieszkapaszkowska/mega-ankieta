from iss.surveys.abstractDatasourceSubclass import AbstractDatasourceSubclass


class TestDatasource(AbstractDatasourceSubclass):
    args_data = {
        'name': {
            'type': 'string',
            'required': 1
        },
    }

    unnamed_args = ['name']
