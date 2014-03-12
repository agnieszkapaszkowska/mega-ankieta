#!/usr/bin/env python
from __future__ import print_function
import os, sys
from iss.surveys.parser import Parser
from iss.surveys.survey import Survey
from iss.surveys.pythonTests import testCases

errors = 0
sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0) #unbuffered stdout

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

		if len(sys.argv) == 1 or (not sys.argv[1] in ['-v', '--verbose']):
			print('x', end='')
			continue

		wrongTestNum = "\nTest %s error:\n" % i
		errorDetails = "Survey text:\n%s\n" % testCases[i]

		print(wrongTestNum + errorDetails)
		raise

summary = "\n\nAll tests completed (%s test):\n%s errors\n%s passed\n" % \
		(len(testCases), errors, len(testCases) - errors)

print(summary)
