import unittest

import sys
import os
from io import StringIO

sys.path.insert(1, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import src.parser.earley_parser as earley_parser
import src.grammar as grammar
import src.analyzers.lexical_analyzer as lexical_analyzer
from src.syntax_tree import MyNodeClass
from src.parser.situation import Situation



class TestParserEarleyParser(unittest.TestCase):

    def test_init(self):
        la = lexical_analyzer.CppLexAnalyzer()
        term1 = grammar.Term('test1')
        term2 = grammar.Term('test2')

        rule1 = grammar.Rule(term1, [term2])
        g = grammar.Grammar([rule1], [term1], [term2], term1)

        ep = earley_parser.EarleyParser(la, g)

        self.assertEqual(ep.pi, None)
        self.assertEqual(ep.tree, None)
        self.assertEqual(ep.lex_list, [])
        self.assertEqual(ep._EarleyParser__grammar, g)
        self.assertEqual(ep._EarleyParser__lex, la)

    def test_get_new_lex(self):
        la = lexical_analyzer.CppLexAnalyzer()
        term1 = grammar.Term('test1')
        term2 = grammar.Term('test2')

        rule1 = grammar.Rule(term1, [term2])
        g = grammar.Grammar([rule1], [term1], [term2], term1)

        ep = earley_parser.EarleyParser(la, g)
        ep.lex_list = [[term1, term2]]
        ep.tree = MyNodeClass(term1, 0, 365, 0, children=[MyNodeClass(term1, 0, 365, 0)])

        a = ep.get_new_lex()

        self.assertEqual(a, [[None, "test1", None]])

    def test_r(self):
        la = lexical_analyzer.CppLexAnalyzer()
        term1 = grammar.Term('test1')
        term2 = grammar.Term('test2')

        rule1 = grammar.Rule(term1, [term2])
        g = grammar.Grammar([rule1], [term1], [term2], term1)

        ep = earley_parser.EarleyParser(la, g)
        ep.lex_list = [[term1, term2]]

        pi = []
        j = 0
        s = Situation(0, term1, [term2], [])
        states = []

        capturedOutput = StringIO()
        o = sys.stdout
        sys.stdout = capturedOutput

        ep.R(pi, states, s, j)

        sys.stdout = o
        a = capturedOutput.getvalue()

        self.assertEqual(a, "k = 0\nc = 0\n")

    def test_print_tree(self):
        la = lexical_analyzer.CppLexAnalyzer()
        term1 = grammar.Term('test1')
        term2 = grammar.Term('test2')

        rule1 = grammar.Rule(term1, [term2])
        g = grammar.Grammar([rule1], [term1], [term2], term1)

        ep = earley_parser.EarleyParser(la, g)
        ep.lex_list = [[term1, term2]]
        ep.tree = MyNodeClass(term1, 0, 365, 0, children=[MyNodeClass(term1, 0, 365, 0)])

        capturedOutput = StringIO()
        o = sys.stdout
        sys.stdout = capturedOutput

        ep.print_tree()

        sys.stdout = o
        a = capturedOutput.getvalue()

        self.assertEqual(a, "test1    0 365 0\n└── test1 0 365 0\n")



