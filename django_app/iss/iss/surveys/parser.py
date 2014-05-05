import os
from simpleparse import generator
from mx.TextTools import TextTools

parse_tree = {
    'PROD_NAME': 0,
    'START': 1,
    'STOP': 2,
    'CHILDREN_TREES': 3
}


class Parser:
    grammar_file = '/grammar.def'
    start_prod_name = 'survey'

    @staticmethod
    def parse(text):
        grammar_path = os.path.abspath(os.path.dirname(__file__))
        with open(grammar_path + Parser.grammar_file, 'r') as grammar:
            parser = generator.buildParser(grammar.read()).\
                parserbyname(Parser.start_prod_name)

        return TextTools.tag(text, parser)
