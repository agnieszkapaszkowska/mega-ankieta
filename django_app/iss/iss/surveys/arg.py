from iss.surveys.parser import parse_tree
from iss.surveys.survey import Survey


class Arg:
    type_synonims = {
        "extendedString":   ["extendedString", "string", "varId",
                             "structElem"],
        "string":           ["string", "varId", "structElem"],
        "number":           ["number", "arythmExpr", "varId", "structElem"],
        "bool":             ["condition", "bool", "varId", "structElem"],
        "listWithTuples":   ["listWithTuples", "iterator", "varId",
                             "structElem"],
        "listWithoutTuples": ["listWithoutTuples", "iterator", "varId",
                              "structElem"],
        "tupleWithLists":   ["tupleWithLists", "iterator", "varId",
                             "structElem"],
        "tupleWithoutLists": ["tupleWithoutLists", "iterator", "varId",
                              "structElem"],
        "iterator":         ["iterator", "varId", "structElem"],
        "datasource":       ["datasource", "varId", "structElem"],
    }

    def __init__(self, result_tree):
        children_trees = result_tree[parse_tree['CHILDREN_TREES']]
        self.value_tree = children_trees[-1]
        self.data = None

        if len(children_trees) == 2:
            start = children_trees[0][parse_tree['START']]
            stop = children_trees[0][parse_tree['STOP']]
            self.name = Survey.text[start:stop]
        else:
            self.name = ''

    def set_data(self, name, data):
        self.name = name
        self.data = data

    def get_name(self):
        return self.name

    def generate_js(self):
        value_type = self.value_tree[parse_tree['PROD_NAME']]

        if (self.data
                and not value_type in self.type_synonims[self.data['type']]):
            raise Exception('Argument ' + self.name
                            + ' should be one of types: '
                            + str(self.type_synonims[self.data['type']])
                            + ' not ' + value_type)

        value = Survey.string_to_class(value_type)(self.value_tree, self.data)
        js = value.generate_js()

        return ((self.name + ': ') if len(self.name) else '') + js
