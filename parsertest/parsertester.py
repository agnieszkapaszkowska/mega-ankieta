from __future__ import print_function
import os
from sys import stdin, stdout, stderr, argv
from simpleparse.parser import Parser
from parserTests import testCases

decl = open('grammar.def').read()
parser = Parser(decl)

for i in range(0, len(testCases)):
	input, production, expectedResult = testCases[i]
	success, children, nextCharacter = parser.parse(input,
			production=production)
	try:
		assert success == expectedResult and ((expectedResult == 1 and nextCharacter==len(input)) or expectedResult == 0)
		print(".", end=""),
	except AssertionError:
		if len(argv) > 1 and (argv[1] == '-v' or argv[1] == '--verbose'):
			if expectedResult == 1:
				print("\nTest %s error:\nWasn't able to parse %s as a %s (%s chars parsed of %s),"
				"returned value was %s""" % 
				( i, input, production, nextCharacter, len(input), 
					(success, children, nextCharacter)))
				break
			else:
				print("\nTest %s error:\nShouldn't have parsed %s as a %s (%s chars parsed of %s),"
				"returned value was %s""" % 
				( i, input, production, nextCharacter, len(input), 
					(success, children, nextCharacter)))
				break


		else:
			print('x', end='')
