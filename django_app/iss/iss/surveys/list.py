from iss.surveys.abstractParametrisedObject import AbstractParametrisedObject
from iss.surveys.parser import parse_tree
from iss.surveys.arg import Arg


class List(AbstractParametrisedObject):

    def generate_js(self):
        return 'function() { return ' + self.generate_simple_js() + '}'

    def generate_simple_js(self):
        self.create_args()

        return "[" + ', '.join(self.js_args_list) + "]"

    def create_args(self):
        for arg_tree in self.result_tree[parse_tree['CHILDREN_TREES']]:
            js, arg_name = self.generate_arg(arg_tree)
            self.add_to_js_args_list(js, arg_name)

    def generate_arg(self, arg_tree):
        arg = Arg(arg_tree)
        arg.set_data('', self.args_data)

        return arg.generate_js(), arg.get_name()
