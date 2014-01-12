from __future__ import print_function
import os
from sys import stdin, stdout, stderr
from simpleparse import generator
from mx.TextTools import TextTools
import re

input = stdin.read()

def print_tree(tree, level):
	if tree == None or tree == []:
		pass
	else:
		for el in tree:
			print(level * "\t" + "{0} ({1}-{2} \"{3}\")".format(el[0],el[1],el[2], re.sub(r'\n', r'\\n', input[el[1]:el[2]])))
			print_tree(el[3], level + 1)


decl = open('grammar.def').read()
parser = generator.buildParser(decl).parserbyname('survey')
success, resultTrees, nextCharacter = TextTools.tag(input, parser)

print_tree(resultTrees, 0)
#print(resultTrees)


