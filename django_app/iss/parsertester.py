#!/usr/bin/env python
from __future__ import print_function
import os, sys
from simpleparse.parser import Parser
from iss.surveys.parserTests import test_cases
from simpleparse.error import ParserSyntaxError

with open('iss/surveys/grammar.def') as decl:
    parser = Parser(decl.read())

errors = 0
sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0) #unbuffered stdout

for i in range(0, len(test_cases)):
    input, prod, should_succeed = test_cases[i]

    try:
        success, children, next_character = parser.parse(input, production=prod)
        assert (success == should_succeed) or ((not should_succeed) and (next_character < len(input)))
        assert (should_succeed and next_character == len(input)) or (not should_succeed)

        print(".", end="")

    except (AssertionError, ParserSyntaxError):
        if not should_succeed:
            print(".", end="")
            continue

        errors += 1

        if len(sys.argv) == 1 or (not sys.argv[1] in ['-v', '--verbose']):
            print('x', end='')
            continue

        wrong_test_num = "\nTest %s error:\n" % i
        error_type = "wasn't able to parse " if should_succeed else "Shouldn't have parsed "
        error_details = "%s as %s (%s chars parsed of %s), parsedTree: %s\n" % \
                (input, prod, next_character, len(input), children)

        print(wrong_test_num + error_type + error_details)
        raise

if errors == 0 or (len(sys.argv) == 1 or (not sys.argv[1] in ['-v', '--verbose'])):
    summary = "\n\nAll tests completed (%s tests):\n%s errors\n%s passed\n" % \
            (len(test_cases), errors, len(test_cases) - errors)

    print(summary)
