from iss.surveys.survey import Survey
from iss.surveys.parser import parse_tree
from iss.surveys.value import Value


class StringConditional(Value):

    def generate_simple_js(self):
        js_parts = []

        for production in self.result_tree[parse_tree['CHILDREN_TREES']]:
            prod_class = Survey.string_to_class(
                production[parse_tree['PROD_NAME']])

            js_parts.append(prod_class(production).generate_simple_js())

        has_else = len(js_parts) == 3

        return '((' + js_parts[0] + ')?(' + js_parts[1] + '):(' +\
            (js_parts[2] if has_else else '""') + '))'
