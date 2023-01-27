import sys

import copy
from anytree import RenderTree

from src import grammar as gr
from src.analyzers import lexical_analyzer as lex

from src.parser.earley import Earley
from src.parser.situation import Situation

from src.syntax_tree import MyNodeClass
from src.analyzers.semantics_analyzer import CppSemanticsAnalyzer


class EarleyParser:
    # __earley = Earley()

    def __init__(self, lexer: lex.CppLexAnalyzer, g: gr.Grammar):
        self.__lex = lexer
        self.__grammar = g
        self.pi = None

        self.__earley = Earley()
        self.tree = None
        self.lex_list = []

    def parse(self, file):
        self.lex_list = self.__lex.analysis(file)
        state_list = self.__earley.start(self.__grammar, self.lex_list)

        if type(state_list) is str:
            print(state_list)
            print("Stop parsing")
            sys.exit()

        print(str(self.__grammar.rules_count()))
        self.pi = self.start_r(state_list)
        self.print_rules()
        print("_______TREE________")
        self.grow_tree()
        sem = CppSemanticsAnalyzer(self.tree)

        if sem.check_semantic():
            self.print_tree()
            # sys.exit()
            return self.get_new_lex()

        print("_______OPTIMIZER________")
        sem.optimizer()
        self.print_tree()
        return self.get_new_lex()

    def get_new_lex(self):
        leaves = self.tree.leaves
        res = []

        for leave in leaves:
            res.append([leave.term.lex, leave.term.value, leave.term.line])

        return res

    def R(self, pi, states, s: Situation, j: int):
        rule = gr.Rule(copy.deepcopy(s.left), copy.deepcopy(s.beforeDot))
        pi.append(self.__grammar.find_rule_number(rule))
        k = len(s.beforeDot)
        c = j

        print("k = " + str(k))
        print("c = " + str(c))

        while k > 0:
            right_term = rule.right[k - 1]
            print(right_term.value)

            if self.__grammar.is_terminal(right_term):
                k = k - 1
                c = c - 1

                print("k = " + str(k))
                print("c = " + str(c))

            elif self.__grammar.is_nonterminal(right_term):
                c, k = self.__find_situation_in_i(c, k, pi, s, states)
        return pi

    def __find_situation_in_i(self, c, k, pi, s, states):
        """
        Находим ситуации в I[c] и I[r]
        """

        # Находим ситуацию в I[c]
        Xk = s.beforeDot[k - 1].value
        A = s.left.value
        r = None
        search_state = None
        search_flag = False
        for st in states[c]:
            if search_flag:
                break
            if not st.afterDot and st.left.value == Xk:
                r = st.get_k()
                print("r = " + str(r))
                # находим ситуацию в I[r]
                print("-------")
                for nst in states[r]:
                    if nst.left.value == s.left.value \
                            and nst.afterDot and nst.afterDot[0].value == Xk \
                            and len(nst.beforeDot) == k - 1:
                        search_state = st
                        search_flag = True
                        break
        self.R(pi, states, search_state, c)
        k = k - 1
        c = r
        return c, k

    def start_r(self, state_list):
        state = None
        for sit in state_list[-1]:
            if not sit.afterDot and sit.left.value == self.__grammar.s.value:
                state = sit
        if state is not None:
            return self.R([], state_list, state, len(state_list) - 1)
        else:
            print("Error in parsing - could not get this program from grammar")
            sys.exit()

    def print_rules(self) -> None:
        for number in self.pi:
            self.__grammar.print_rule(number)

    def grow_tree(self) -> None:
        self.pi.reverse()
        first_rule = self.__grammar.get_rule(self.pi.pop())
        self.tree = MyNodeClass(copy.deepcopy(first_rule.left), 0, len(self.pi) + 1, 0)
        new_nodes = []

        print(self.lex_list)

        for index, item in enumerate(first_rule.right):
            new_nodes.append(MyNodeClass(copy.deepcopy(item), 1, len(self.pi), index, self.tree))
        for item in reversed(new_nodes):
            self.add_children(item.term, item, item.deep)
        self.print_tree()

    def add_children(self, term, parent, depth) -> None:
        if self.__grammar.is_terminal(term):
            curr_lex = self.lex_list.pop()
            term.setlex(curr_lex[0])
            term.setline(curr_lex[2])
            return
        else:
            rule = self.__grammar.get_rule(self.pi.pop())
            new_nodes = []

            for index, item in enumerate(rule.right):
                new_nodes.append(MyNodeClass(copy.deepcopy(item), depth + 1, len(self.pi), index, parent))

            for item in reversed(new_nodes):
                self.add_children(item.term, item, item.deep)

    def print_tree(self) -> None:
        for pre, fill, node in RenderTree(self.tree):
            tree_str = u"%s%s" % (pre, node.term.value)

            if node.term.lex is not None:
                print(tree_str.ljust(8), node.term.lex, node.deep, node.pi_stack_number, node.right_number)
            else:
                print(tree_str.ljust(8), node.deep, node.pi_stack_number, node.right_number)
