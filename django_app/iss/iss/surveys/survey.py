import sys
import traceback
from parser import Parser, parseTree


class Survey:
    text = ''
    surveyVar = 'iss.survey'

    @staticmethod
    def generate():
        try:
            success, resultTrees, nextCharacter = Parser.parse(Survey.text)

            if not success or nextCharacter != len(Survey.text):
                raise Exception("Parsing error")

            return '', Survey.generateJS(resultTrees)

        except Exception as e:
            traceback.print_exc(file=sys.stdout)
            return str(e), ''

    @staticmethod
    def generateJS(resultTrees):
        js = "var iss = {};\n" + Survey.surveyVar + " = new iss.lib.Survey();\n"

        for resultTree in resultTrees:
            prodName = resultTree[parseTree['PROD_NAME']]
            production = Survey.stringToClass(prodName)(resultTree)

            js += production.generateJS() + "\n"

        return js

    @staticmethod
    def stringTreeToClass(stringTree, baseClassName = ''):
        from iss.surveys.string import String
        string = String(stringTree).getPythonValue()

        return Survey.stringToClass(string, baseClassName)

    @staticmethod
    def stringToClass(string, baseClassName = ''):
        fileName = string[0].lower() + string[1:] + baseClassName
        className = string[0].upper() + string[1:] + baseClassName

        module = __import__('iss.surveys.' + fileName, globals(), locals(), className)

        return getattr(module, className)
