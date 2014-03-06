#!/usr/bin/env python
from __future__ import print_function
from sys import argv
from iss.surveys.parser import Parser
from iss.surveys.survey import Survey
from iss.surveys.pythonTests import testCases

errors = 0

for i in range(0, len(testCases)):
	try:
		Survey.text = testCases[i]
		success, resultTrees, nextCharacter = Parser.parse(Survey.text)

		if not success or nextCharacter != len(Survey.text):
			raise Exception("Parsing error")

		Survey.generateJS(resultTrees)

		print('.', end='')

	except Exception:
		errors += 1

		if len(argv) == 1 or (not argv[1] in ['-v', '--verbose']):
			print('x', end='')
			continue

		wrongTestNum = "\nTest %s error:\n" % i
		errorDetails = "Survey text:\n%s\n" % testCases[i]

		print(wrongTestNum + errorDetails)
		raise

summary = "\n\nAll tests completed (%s test):\n%s errors\n%s passed\n" % \
		(len(testCases), errors, len(testCases) - errors)

print(summary)
