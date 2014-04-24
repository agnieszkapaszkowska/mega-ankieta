import sys
import traceback
from parser import Parser, parse_tree


class Survey:
    text = ''
    survey_var = 'iss.survey'

    @staticmethod
    def generate():
        try:
            success, result_trees, next_character = Parser.parse(Survey.text)

            if not success or next_character != len(Survey.text):
                raise Exception("Parsing error")

            return '', Survey.generate_js(result_trees)

        except Exception as e:
            traceback.print_exc(file=sys.stdout)
            return str(e), ''

    @staticmethod
    def generate_js(result_trees):
        js = Survey.survey_var + " = new iss.lib.Survey();\n"
        return (js + Survey.generate_productions_js(result_trees)
                + Survey.survey_var + ".init();\n")

    @staticmethod
    def generate_productions_js(result_trees):
        js = ''
        for result_tree in result_trees:
            prod_name = result_tree[parse_tree['PROD_NAME']]
            production = Survey.string_to_class(prod_name)(result_tree)

            js += production.generate_js()

        return js

    @staticmethod
    def string_tree_to_class(string_tree, base_class_name=''):
        from iss.surveys.string import String
        string = String(string_tree).get_python_value()

        return Survey.string_to_class(string, base_class_name)

    @staticmethod
    def string_to_class(string, base_class_name=''):
        file_name = string[0].lower() + string[1:] + base_class_name
        class_name = string[0].upper() + string[1:] + base_class_name

        module = __import__(
            'iss.surveys.' + file_name, globals(), locals(), class_name)

        return getattr(module, class_name)
