from iss.surveys.survey import Survey
from iss.surveys.parser import parse_tree


class Value:

    def __init__(self, result_tree, _=None):
        self.result_tree = result_tree

    def generate_js(self):
        return 'function() { return ' + self.generate_simple_js() + ' }'

    def generate_simple_js(self):
        start = self.result_tree[parse_tree['START']]
        stop = self.result_tree[parse_tree['STOP']]

        return Survey.text[start:stop]
