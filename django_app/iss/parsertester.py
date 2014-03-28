#!/usr/bin/env python
from __future__ import print_function
import os, sys
from simpleparse.parser import Parser
from iss.surveys.parserTests import testCases
from simpleparse.error import ParserSyntaxError

with open('iss/surveys/grammar.def') as decl:
    parser = Parser(decl.read())

errors = 0
sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0) #unbuffered stdout

for i in range(0, len(testCases)):
    input, prod, shouldSucceed = testCases[i]

    try:
        success, children, nextCharacter = parser.parse(input, production=prod)
        assert (success == shouldSucceed) or ((not shouldSucceed) and (nextCharacter < len(input)))
        assert (shouldSucceed and nextCharacter == len(input)) or (not shouldSucceed)

        print(".", end="")

    except (AssertionError, ParserSyntaxError):
        if not shouldSucceed:
            print(".", end="")
            continue

        errors += 1

        if len(sys.argv) == 1 or (not sys.argv[1] in ['-v', '--verbose']):
            print('x', end='')
            continue

        wrongTestNum = "\nTest %s error:\n" % i
        errorType = "Wasn't able to parse " if shouldSucceed else "Shouldn't have parsed "
        errorDetails = "%s as %s (%s chars parsed of %s), parsedTree: %s\n" % \
                (input, prod, nextCharacter, len(input), children)

        print(wrongTestNum + errorType + errorDetails)
        raise

if errors == 0 or (len(sys.argv) == 1 or (not sys.argv[1] in ['-v', '--verbose'])):
    summary = "\n\nAll tests completed (%s tests):\n%s errors\n%s passed\n" % \
            (len(testCases), errors, len(testCases) - errors)

    print(summary)
