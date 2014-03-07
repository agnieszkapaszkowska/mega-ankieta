import sys
import traceback
from parser import Parser

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

        for prodName, start, stop, childrenTrees in resultTrees:
            production = Survey.stringToClass(prodName)((prodName, start, stop, childrenTrees))
            js += production.getJS() + "\n"

        return js

    @staticmethod
    def stringToClass(string):
        className = Survey.stringToClassName(string)

        return getattr(__import__('iss.surveys.' + string, globals(), locals(), className), className)

    @staticmethod
    def stringToClassName(string):
        return string[0].upper() + string[1:]
