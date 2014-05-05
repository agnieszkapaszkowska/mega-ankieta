from iss.surveys.abstractParametrisedObject import AbstractParametrisedObject
from iss.surveys.survey import Survey
from iss.surveys.parser import parse_tree
from iss.surveys.varId import VarId
from iss.surveys.value import Value


class Assignment(AbstractParametrisedObject):

    def generate_js(self):
        value_tree = self.result_tree[
            parse_tree['CHILDREN_TREES']][self.value_index]
        if value_tree[parse_tree['PROD_NAME']] == 'widget':
            return self.get_widget_value_js()

        var_js = self.get_assignment_var_js()
        value_js = self.get_assignment_value_js()

        return (Survey.survey_var + ".addAssignment( function() {"
                + var_js + ' = ' + value_js + '() });\n')

    def get_assignment_var_js(self):
        var_tree = self.result_tree[parse_tree['CHILDREN_TREES']][
            self.var_index]
        var_id = VarId(var_tree)

        return var_id.generate_simple_js()

    def get_assignment_value_js(self):
        value_tree = self.result_tree[
            parse_tree['CHILDREN_TREES']][self.value_index]
        prod_name = value_tree[parse_tree['PROD_NAME']]
        production = Survey.string_to_class(prod_name)(value_tree)

        return production.generate_js()

    def get_widget_value_js(self):
        children_trees = self.result_tree[parse_tree['CHILDREN_TREES']]

        value_tree = children_trees[self.value_index]
        var_tree = children_trees[self.var_index]

        var_id = Value(var_tree).generate_simple_js()
        widget = Survey.string_to_class('widget')(
            value_tree, additional_js_args=['resultVarName: "' + var_id + '"'])

        return widget.generate_js()
