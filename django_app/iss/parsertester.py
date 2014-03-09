#!/usr/bin/env python
from __future__ import print_function
import os
from sys import argv
from simpleparse.parser import Parser
from iss.surveys.parserTests import testCases

with open('iss/surveys/grammar.def') as decl:
	parser = Parser(decl.read())

errors = 0

for i in range(0, len(testCases)):
	input, prod, shouldSucceed = testCases[i]
	success, children, nextCharacter = parser.parse(input, production=prod)
	try:
		assert (success == shouldSucceed) or ((not shouldSucceed) and (nextCharacter < len(input)))
		assert (shouldSucceed and nextCharacter == len(input)) or (not shouldSucceed)

		print(".", end="")

	except AssertionError:
		errors += 1

		if len(argv) == 1 or (not argv[1] in ['-v', '--verbose']):
			print('x', end='')
			continue

		wrongTestNum = "\nTest %s error:\n" % i
		errorType = "Wasn't able to parse " if shouldSucceed else "Shouldn't have parsed "
		errorDetails = "%s as %s (%s chars parsed of %s), parsedTree: %s\n" % \
				(input, prod, nextCharacter, len(input), children)

		print(wrongTestNum + errorType + errorDetails)
		break

if errors == 0 or (len(argv) == 1 or (not argv[1] in ['-v', '--verbose'])):
	summary = "\n\nAll tests completed (%s tests):\n%s errors\n%s passed\n" % \
			(len(testCases), errors, len(testCases) - errors)

	print(summary)
