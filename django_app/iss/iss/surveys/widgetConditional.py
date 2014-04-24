from iss.surveys.abstractParametrisedObject import AbstractParametrisedObject
from iss.surveys.condition import Condition
from iss.surveys.survey import Survey
from parser import parse_tree


class WidgetConditional(AbstractParametrisedObject):

    def generate_js(self):
        condition = ''
        conditions = []
        js = []
        for component in self.result_tree[parse_tree['CHILDREN_TREES']]:
            if component[parse_tree['PROD_NAME']] == 'condition':
                condition = Condition(
                    component).generate_js()
            else:
                if condition == '':
                    condition = "function() { return true }"
                js.append("{condition: function() { return "
                          + condition + "()" + (
                              " && " + " && ".join(conditions)
                              if len(conditions) > 0 else "")
                          + " }, body: function() { "
                          + Survey.generate_productions_js(
                              component[parse_tree['CHILDREN_TREES']])
                          + "}}")
                conditions.append("!(" + condition + "())")
                condition = ''
        return (Survey.survey_var
                + ".addWidgetConditional([" + ",".join(js) + "]);\n")
