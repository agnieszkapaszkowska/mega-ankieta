from iss.surveys.arg import Arg
from iss.surveys.string import String
from iss.surveys.survey import Survey
from iss.surveys.parser import parse_tree


class AbstractParametrisedObject:

    args_data = None

    def __init__(self, result_tree, args_data=None, **kwargs):
        self.result_tree = result_tree

        self.found_unnamed_args = 0
        self.found_args_names = []
        self.js_args_list = []

        if 'additional_js_args' in kwargs:
            self.js_args_list = kwargs['additional_js_args']

        if not args_data:
            args_data = self.args_data
            if not args_data:
                return

        if 'args' in args_data:
            self.args_data = args_data['args']

        if 'unnamed_args' in args_data:
            self.unnamed_args = args_data['unnamed_args']

    def generate_js(self):
        string_tree = self.result_tree[parse_tree['CHILDREN_TREES']][0]
        self.result_tree[parse_tree['CHILDREN_TREES']].pop(0)

        widget_subclass = Survey.string_tree_to_class(
            string_tree, self.get_class_name())
        return widget_subclass(self.result_tree, additional_js_args=self.js_args_list).generate_js()

    def generate_simple_js(self):
        self.create_args()

        return '{' + ', '.join(self.js_args_list) + '}'

    def create_args(self):
        if self.args_data:
            self.create_typed_args()
        else:
            self.create_untyped_args()

    def create_typed_args(self):
        for arg_tree in self.result_tree[parse_tree['CHILDREN_TREES']]:
            js, arg_name = self.generate_arg(arg_tree)
            self.check_arg(arg_name)
            self.add_to_js_args_list(js, arg_name)

        self.check_args()
        self.add_defaults_to_js_args_list()

    def create_untyped_args(self):
        i = 0
        for arg_tree in self.result_tree[parse_tree['CHILDREN_TREES']]:
            js, arg_name = self.generate_arg(arg_tree)
            if arg_name:
                self.add_to_js_args_list(js, arg_name)
            else:
                self.add_untyped_to_js_args_list(js, str(i))
                i += 1

    def generate_arg(self, arg_tree):
        arg = Arg(arg_tree)
        arg.set_data(*self.get_arg_data(arg.get_name()))

        return arg.generate_js(), arg.get_name()

    def get_arg_data(self, arg_name):
        if not self.args_data:
            return arg_name, None

        if not len(arg_name):
            if len(self.unnamed_args) == self.found_unnamed_args:
                raise Exception(self.get_class_name() +
                                " accepts only " + str(len(self.unnamed_args)) +
                                " unnamed arguments")

            arg_name = self.unnamed_args[self.found_unnamed_args]

        if arg_name in self.args_data:
            return arg_name, self.args_data[arg_name]

        raise Exception(self.get_class_name() +
                        " does not accept parameter named " + arg_name)

    def add_to_js_args_list(self, js, arg_name):
        if len(arg_name):
            self.found_args_names.append(arg_name)

            if (hasattr(self, 'unnamed_args')
                    and arg_name == self.unnamed_args[self.found_unnamed_args]):
                self.found_unnamed_args = self.get_next_unnamed_arg_index()

        self.js_args_list.append(js)

    def add_untyped_to_js_args_list(self, js, arg_name):
        self.js_args_list.append(arg_name + ':' + js)

    def get_next_unnamed_arg_index(self):
        next_index = self.found_unnamed_args + 1

        while next_index != len(self.unnamed_args) and\
                self.unnamed_args[next_index] in self.found_args_names:
            next_index += 1

        return next_index

    def check_arg(self, arg_name):
        if arg_name in self.found_args_names:
            raise Exception(
                "You cannot use two same-named arguments in one parametrised object")

    def check_args(self):
        for name in self.args_data:
            if self.args_data[name]['required'] and not name in self.found_args_names:
                raise Exception(
                    'Required argument "' + name + '" wasn\'t supplied')

    def add_defaults_to_js_args_list(self):
        for name in self.args_data:
            if not self.args_data[name]['required'] and not name in self.found_args_names:
                self.js_args_list.append(
                    name + ": function() { return " + self.args_data[name]['default'] + " }")

    def get_class_name(self):
        return self.__class__.__name__
