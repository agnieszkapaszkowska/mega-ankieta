from simpleparse import generator
from mx.TextTools import TextTools
from iss.surveys.widget import Widget
import re


class JSGenerator:
    grammarName = 'iss/surveys/grammar.def'
    startSymbolName = 'survey'

    def generate(self, text):
        success, resultTrees, nextCharacter = self.parse(text)
        if not success or nextCharacter != len(text):
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
        jsScript = "var survey = new Survey();\n"
        error = "0"
        for (name, start, stop, childTrees) in resultTrees:
            error, code = getattr(
                self, self.convert_from_camelcase(name))(childTrees)
            if error != "0":
                return error, ""
            jsScript += code
        return error, jsScript

    def assignment_left(self, resultTrees):
        error, code = self.widget(resultTrees[1][3])
        code += ""  # assignment in onchange
        return error, "assignmentLeft\n"
    
    def assignment_right(self, resultTrees):
        error, code = self.widget(resultTrees[0][3])
        code += ""  # assignment in onchange
        return error, "assignmentRight\n"

    def widget(self, resultTrees):
        return "0", "widget\n"

    def widget_conditional(self, resultTrees):
        return "0", "widgetConditional\n"

    def convert_from_camelcase(self, name):
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()