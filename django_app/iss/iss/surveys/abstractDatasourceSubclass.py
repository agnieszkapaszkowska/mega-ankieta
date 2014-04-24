from iss.surveys.datasource import Datasource


class AbstractDatasourceSubclass(Datasource):

    def generate_js(self):
        simple_js = self.generate_simple_js()

        return "function() {return " + simple_js + "}"

    def generate_simple_js(self):
        return ('iss.lib.datasources.' + self.get_class_name()
                + '(' + Datasource.generate_simple_js(self) + ')')
