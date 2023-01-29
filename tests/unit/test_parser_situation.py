import unittest



import src.parser.situation as situation
from src.grammar import Term, Rule


class TestParserSituation(unittest.TestCase):

    def test_init(self):
        term1 = Term('test1')
        term2 = Term('test2')

        s = situation.Situation(0, term1, [term2])

        self.assertEqual(s.k, 0)
        self.assertEqual(s.left, term1)
        self.assertEqual(s.afterDot, [term2])
        self.assertEqual(s.beforeDot, [])

    def test_move_dot(self):
        term1 = Term('test1')
        term2 = Term('test2')

        s = situation.Situation(0, term1, [term2])
        s.move_dot()

        self.assertEqual(s.k, 0)
        self.assertEqual(s.left, term1)
        self.assertEqual(s.afterDot, [])
        self.assertEqual(s.beforeDot, [term2])

    def test_set_k(self):
        term1 = Term('test1')
        term2 = Term('test2')

        s = situation.Situation(0, term1, [term2])
        s.set_k(1)

        self.assertEqual(s.k, 1)
        self.assertEqual(s.left, term1)
        self.assertEqual(s.afterDot, [term2])
        self.assertEqual(s.beforeDot, [])

    def test_get_k(self):
        term1 = Term('test1')
        term2 = Term('test2')

        s = situation.Situation(0, term1, [term2])

        self.assertEqual(s.get_k(), 0)
