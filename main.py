from src.parser.earley_parser import *
import src.analyzers.lexical_analyzer as lex
import src.cpp_grammar as cpp_grammar
from src.code_generator.generator import *

import pprint

pp = pprint.PrettyPrinter(width=80, compact=True)

Gen = Generator()
myParser = EarleyParser(lex.CppLexAnalyzer(), cpp_grammar.set_cpp())

f = open('test_cases/main.cpp', 'r')
parsed = myParser.parse(f)
# print(parsed)
print("parse result:")
pp.pprint(parsed)

Gen.late(parsed)

f.close()