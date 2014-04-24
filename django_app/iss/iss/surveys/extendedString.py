from iss.surveys.survey import Survey
from iss.surveys.parser import parse_tree
from iss.surveys.value import Value


class ExtendedString(Value):

    def generate_js(self):
        return "function() { with (iss.vars) { return " + self.generate_simple_js() + '} }'

    def generate_simple_js(self):
        text = []

        for production in self.result_tree[parse_tree['CHILDREN_TREES']]:
            prod_class = Survey.string_to_class(
                production[parse_tree['PROD_NAME']])

            prod_js = prod_class(production).generate_simple_js()
            if production[parse_tree['PROD_NAME']] == 'innerString':
                prod_js = '"' + prod_js + '"'
            text.append(prod_js)

        return ' + '.join(text)
