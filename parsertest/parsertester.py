from __future__ import print_function
import os
from sys import stdin, stdout, stderr, argv
from simpleparse.parser import Parser
from parserTests import testCases

decl = open('grammar.def').read()
parser = Parser(decl)

for i in range(0, len(testCases)):
	input, production, expectedResult = testCases[i]
	success, children, nextCharacter = parser.parse(input, production=production)
	try:
		assert success == expectedResult and nextCharacter==len(input)
		print(".", end=""),
	except AssertionError:
		if len(argv) > 1 and (argv[1] == '-v' or argv[1] == '--verbose'):
			print("""\nTest %s error:\nWasn't able to parse %s as a %s (%s chars parsed of %s), returned value was %s""" % ( i, input, production, nextCharacter, len(input), (success, children, nextCharacter)))
			break
		else:
			print('x', end='')
