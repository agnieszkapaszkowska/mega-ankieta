from simpleparse import generator
from mx.TextTools import TextTools

parseTree = {\
        'PROD_NAME': 0,\
        'START': 1,\
        'STOP': 2,\
        'CHILDREN_TREES': 3\
        }

class Parser:
    grammarFile = 'iss/surveys/grammar.def'
    startProdName = 'survey'

    @staticmethod
    def parse(text):
        with open(Parser.grammarFile, 'r') as grammar:
            parser = generator.buildParser(grammar.read()).\
                    parserbyname(Parser.startProdName)

        return TextTools.tag(text, parser)
