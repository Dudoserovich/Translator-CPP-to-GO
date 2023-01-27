import unittest

import sys
import os

sys.path.insert(1, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import src.grammar as grammar


class TestTerm(unittest.TestCase):

    def test_init_min(self):
        term = grammar.Term('test')
        self.assertEqual(term.value, 'test')
        self.assertEqual(term.line, None)
        self.assertEqual(term.lex, None)

    def test_init_max(self):
        term = grammar.Term('test', 1, 2)
        self.assertEqual(term.value, 'test')
        self.assertEqual(term.line, 1)
        self.assertEqual(term.lex, 2)

    def test_set_lex(self):
        term = grammar.Term('test')
        term.set_lex(1)
        self.assertEqual(term.lex, 1)

    def test_set_line(self):
        term = grammar.Term('test')
        term.set_line(1)
        self.assertEqual(term.line, 1)

    def test_get_value(self):
        term = grammar.Term('test')
        self.assertEqual(term.get_value(), 'test')

    def test_get_lex(self):
        term = grammar.Term('test')
        self.assertEqual(term.get_lex(), None)

    def test_get_line(self):
        term = grammar.Term('test')
        self.assertEqual(term.get_line(), None)

    def test_set_lex(self):
        term = grammar.Term('test')
        term.set_lex(1)
        self.assertEqual(term.lex, 1)

    def test_set_line(self):
        term = grammar.Term('test')
        term.set_line(1)
        self.assertEqual(term.line, 1)


class TestRule(unittest.TestCase):

    def test_init_min(self):
        term = grammar.Term('test')
        rule = grammar.Rule(term, [])
        self.assertEqual(rule.left, term)
        self.assertEqual(rule.right, [])

    def test_init_max(self):
        term = grammar.Term('test')
        rule = grammar.Rule(term, [term, term])
        self.assertEqual(rule.left, term)
        self.assertEqual(rule.right, [term, term])

    def test_get_left(self):
        term = grammar.Term('test')
        rule = grammar.Rule(term, [])
        self.assertEqual(rule.get_left(), term)

    def test_get_right(self):
        term = grammar.Term('test')
        rule = grammar.Rule(term, [])
        self.assertEqual(rule.get_right(), [])


class TestGrammar(unittest.TestCase):

    def test_init(self):
        term1 = grammar.Term('test1')
        term2 = grammar.Term('test2')

        rule1 = grammar.Rule(term1, [term2])
        grammar_ = grammar.Grammar([rule1], [term1], [term2], term1)

        self.assertEqual(grammar_.rules, [rule1])
        self.assertEqual(grammar_.nonterminal, [term1])
        self.assertEqual(grammar_.terminal, [term2])
        self.assertEqual(grammar_.s, term1)

    def test_rules_count(self):
        term1 = grammar.Term('test1')
        term2 = grammar.Term('test2')

        rule1 = grammar.Rule(term1, [term2])
        grammar_ = grammar.Grammar([rule1], [term1], [term2], term1)

        self.assertEqual(grammar_.rules_count(), 1)

    def test_rule_equals(self):
        term1 = grammar.Term('test1')
        term2 = grammar.Term('test2')

        rule1 = grammar.Rule(term1, [term2])
        rule2 = grammar.Rule(term1, [term2])
        grammar_ = grammar.Grammar([rule1], [term1], [term2], term1)

        self.assertEqual(grammar_.rule_equals(rule1, rule2), True)

    def test_find_rule_number(self):
        term1 = grammar.Term('test1')
        term2 = grammar.Term('test2')

        rule1 = grammar.Rule(term1, [term2])
        grammar_ = grammar.Grammar([rule1], [term1], [term2], term1)

        self.assertEqual(grammar_.find_rule_number(rule1), 0)

    def test_find_rule_number_not_found(self):
        term1 = grammar.Term('test1')
        term2 = grammar.Term('test2')

        rule1 = grammar.Rule(term1, [term2])
        grammar_ = grammar.Grammar([rule1], [term1], [term2], term1)

        self.assertEqual(grammar_.find_rule_number(grammar.Rule(term1, [])), -1)

    def test_get_rules(self):
        term1 = grammar.Term('test1')
        term2 = grammar.Term('test2')

        rule1 = grammar.Rule(term1, [term2])
        grammar_ = grammar.Grammar([rule1], [term1], [term2], term1)

        self.assertEqual(grammar_.get_rules(), [rule1])

    def test_get_terms(self):
        term1 = grammar.Term('test1')
        term2 = grammar.Term('test2')

        rule1 = grammar.Rule(term1, [term2])
        grammar_ = grammar.Grammar([rule1], [term1], [term2], term1)

        for term in grammar_.get_terms():
            self.assertTrue(term in [term1, term2])

    def test_get_s(self):
        term1 = grammar.Term('test1')
        term2 = grammar.Term('test2')

        rule1 = grammar.Rule(term1, [term2])
        grammar_ = grammar.Grammar([rule1], [term1], [term2], term1)

        self.assertEqual(grammar_.get_s(), term1)

    def test_get_terminal(self):
        term1 = grammar.Term('test1')
        term2 = grammar.Term('test2')

        rule1 = grammar.Rule(term1, [term2])
        grammar_ = grammar.Grammar([rule1], [term1], [term2], term1)

        self.assertEqual(grammar_.get_terminal(), [term2])

    def test_get_nonterminal(self):
        term1 = grammar.Term('test1')
        term2 = grammar.Term('test2')

        rule1 = grammar.Rule(term1, [term2])
        grammar_ = grammar.Grammar([rule1], [term1], [term2], term1)

        self.assertEqual(grammar_.get_nonterminal(), [term1])

    def test_is_terminal(self):
        term1 = grammar.Term('test1')
        term2 = grammar.Term('test2')

        rule1 = grammar.Rule(term1, [term2])
        grammar_ = grammar.Grammar([rule1], [term1], [term2], term1)

        self.assertEqual(grammar_.is_terminal(term2), True)

    def test_is_nonterminal(self):
        term1 = grammar.Term('test1')
        term2 = grammar.Term('test2')

        rule1 = grammar.Rule(term1, [term2])
        grammar_ = grammar.Grammar([rule1], [term1], [term2], term1)

        self.assertEqual(grammar_.is_nonterminal(term1), True)

    def test_print_rule(self):
        term1 = grammar.Term('test1')
        term2 = grammar.Term('test2')

        rule1 = grammar.Rule(term1, [term2])
        grammar_ = grammar.Grammar([rule1], [term1], [term2], term1)

        self.assertEqual(grammar_.print_rule(0), '0: test1->test2 ')

    def test_get_rule(self):
        term1 = grammar.Term('test1')
        term2 = grammar.Term('test2')

        rule1 = grammar.Rule(term1, [term2])
        grammar_ = grammar.Grammar([rule1], [term1], [term2], term1)

        self.assertEqual(grammar_.get_rule(0), rule1)
