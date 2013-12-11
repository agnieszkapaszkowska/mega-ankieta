from __future__ import print_function
import os
from sys import stdin, stdout, stderr
from simpleparse import generator
from mx.TextTools import TextTools

input = stdin.read()
decl = open('typographify.def').read()
parser = generator.buildParser(decl).parserbyname('para')
taglist = TextTools.tag(input, parser)
print(taglist)
