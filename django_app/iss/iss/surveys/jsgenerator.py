from simpleparse import generator
from mx.TextTools import TextTools


class JSGenerator:
    grammarName = 'iss/surveys/grammar.def'
    startSymbolName = 'survey'

    def generate(self, text):
        success, resultTrees, nextCharacter = self.parse(text)
        if not success:
            return (self.find_error(
                    text, nextCharacter), '')
        return self.generate_js(resultTrees)

    def parse(self, text):
        decl = open(self.grammarName).read()
        parser = generator.buildParser(
            decl).parserbyname(self.startSymbolName)
        return TextTools.tag(text, parser)

    def find_error(self, text, nextCharacter):
        return 'error'

    def generate_js(self, resultTrees):
        return '0', str(resultTrees)
