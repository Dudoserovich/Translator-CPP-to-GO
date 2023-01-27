import os

import src.cpp_grammar as cpp_grammar
import src.code_generator.generator as gen
import src.parser.earley_parser as ep


def translator(file_name, results_path, tests_path):
    ind = True
    parsed = None

    while ind:
        try:
            kek = ep.EarleyParser(ep.lex.CppLexAnalyzer(), cpp_grammar.set_cpp())
            with open(f'{tests_path}/{file_name}.cpp', 'r') as f:
                parsed = parsed if parsed else kek.parse(f)
                print(f"parse result:\n{parsed}")
                gen.Generator().late(parsed, f"{results_path}/{file_name}.go")
        except FileNotFoundError as e:
            if e.filename == f'{tests_path}/{file_name}.cpp':
                print(f'Файл {tests_path}/{file_name}.cpp не найден!')
                ind = False
            else:
                os.mkdir(results_path)

                kek = ep.EarleyParser(ep.lex.CppLexAnalyzer(), cpp_grammar.set_cpp())
                parsed = None

        else:
            ind = False
