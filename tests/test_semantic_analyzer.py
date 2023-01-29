import unittest
import src.parser.earley_parser as ep
import src.cpp_grammar as cpp_grammar
from src.analyzers.semantics_analyzer import CppSemanticsAnalyzer

class TestCppSemanticsAnalyzer(unittest.TestCase):

    def test_check_semantic_if_then(self, file=f'test_cases/if_then.cpp'):
        kek = ep.EarleyParser(ep.lex.CppLexAnalyzer(), cpp_grammar.set_cpp())
        with open(file, 'r') as f:

            kek.lex_list = kek.get_lex().analysis(f)
            state_list = kek.get_earley().start(kek.get_grammar(), kek.lex_list)
            kek.pi = kek.start_r(state_list)
            kek.print_rules()
            kek.grow_tree()
            sem = CppSemanticsAnalyzer(kek.tree)

            self.assertEqual(sem.check_semantic(), True)

    def test_check_semantic_infernal_loops(self, file=f'test_cases/infernal_loops.cpp'):
        kek = ep.EarleyParser(ep.lex.CppLexAnalyzer(), cpp_grammar.set_cpp())
        with open(file, 'r') as f:

            kek.lex_list = kek.get_lex().analysis(f)
            state_list = kek.get_earley().start(kek.get_grammar(), kek.lex_list)
            kek.pi = kek.start_r(state_list)
            kek.print_rules()
            kek.grow_tree()
            sem = CppSemanticsAnalyzer(kek.tree)

            self.assertEqual(sem.check_semantic(), False)

    def test_check_semantic_lextest(self, file=f'test_cases/lextest.cpp'):
        kek = ep.EarleyParser(ep.lex.CppLexAnalyzer(), cpp_grammar.set_cpp())
        with open(file, 'r') as f:

            kek.lex_list = kek.get_lex().analysis(f)
            state_list = kek.get_earley().start(kek.get_grammar(), kek.lex_list)
            kek.pi = kek.start_r(state_list)
            kek.print_rules()
            kek.grow_tree()
            sem = CppSemanticsAnalyzer(kek.tree)

            self.assertEqual(sem.check_semantic(), False)

    def test_check_semantic_loops(self, file=f'test_cases/loops.cpp'):
        kek = ep.EarleyParser(ep.lex.CppLexAnalyzer(), cpp_grammar.set_cpp())
        with open(file, 'r') as f:

            kek.lex_list = kek.get_lex().analysis(f)
            state_list = kek.get_earley().start(kek.get_grammar(), kek.lex_list)
            kek.pi = kek.start_r(state_list)
            kek.print_rules()
            kek.grow_tree()
            sem = CppSemanticsAnalyzer(kek.tree)

            self.assertEqual(sem.check_semantic(), True)

    def test_check_semantic_main(self, file=f'test_cases/main.cpp'):
        kek = ep.EarleyParser(ep.lex.CppLexAnalyzer(), cpp_grammar.set_cpp())
        with open(file, 'r') as f:

            kek.lex_list = kek.get_lex().analysis(f)
            state_list = kek.get_earley().start(kek.get_grammar(), kek.lex_list)
            kek.pi = kek.start_r(state_list)
            kek.print_rules()
            kek.grow_tree()
            sem = CppSemanticsAnalyzer(kek.tree)

            self.assertEqual(sem.check_semantic(), False)

    def test_check_semantic_operators(self, file=f'test_cases/operators.cpp'):
        kek = ep.EarleyParser(ep.lex.CppLexAnalyzer(), cpp_grammar.set_cpp())
        with open(file, 'r') as f:

            kek.lex_list = kek.get_lex().analysis(f)
            state_list = kek.get_earley().start(kek.get_grammar(), kek.lex_list)
            kek.pi = kek.start_r(state_list)
            kek.print_rules()
            kek.grow_tree()
            sem = CppSemanticsAnalyzer(kek.tree)

            self.assertEqual(sem.check_semantic(), True)

    def test_check_semantic_types(self, file=f'test_cases/types.cpp'):
        kek = ep.EarleyParser(ep.lex.CppLexAnalyzer(), cpp_grammar.set_cpp())
        with open(file, 'r') as f:

            kek.lex_list = kek.get_lex().analysis(f)
            state_list = kek.get_earley().start(kek.get_grammar(), kek.lex_list)
            kek.pi = kek.start_r(state_list)
            kek.print_rules()
            kek.grow_tree()
            sem = CppSemanticsAnalyzer(kek.tree)

            self.assertEqual(sem.check_semantic(), True)
