#!/usr/bin/env python
from __future__ import print_function
import os, sys
from iss.surveys.parser import Parser
from iss.surveys.survey import Survey
from iss.surveys.pythonTests import test_cases

errors = 0
sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0) #unbuffered stdout

for i in range(0, len(test_cases)):
    try:
        Survey.text = test_cases[i]
        success, result_trees, next_character = Parser.parse(Survey.text)

        if not success or next_character != len(Survey.text):
            raise Exception("Parsing error")

        Survey.generate_js(result_trees)

        print('.', end='')

    except Exception:
        errors += 1

        if len(sys.argv) == 1 or (not sys.argv[1] in ['-v', '--verbose']):
            print('x', end='')
            continue

        wrong_test_num = "\nTest %s error:\n" % i
        error_details = "Survey text:\n%s\n" % test_cases[i]

        print(wrong_test_num + error_details)
        raise

summary = "\n\nAll tests completed (%s test):\n%s errors\n%s passed\n" % \
        (len(test_cases), errors, len(test_cases) - errors)

print(summary)
