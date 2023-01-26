# import src.cpp_grammar as cpp_grammar
# from src.code_generator.generator import *
# from src.parser.earley_parser import *

import importlib


def translator(file_name, results_path, tests_path):
    ind = True
    parsed = None

    import src.cpp_grammar as cpp_grammar
    import src.code_generator.generator as gen
    import src.parser.earley_parser as ep

    importlib.reload(cpp_grammar)
    importlib.reload(gen)
    importlib.reload(ep)

    while ind:
        try:
            kek = ep.EarleyParser(ep.lex.CppLexAnalyzer(), cpp_grammar.set_cpp())
            with open(f'{tests_path}/{file_name}.cpp', 'r') as f:
                parsed = parsed if parsed else kek.parse(f)
                print(f"parse result:\n{parsed}")
                if file_name == 'if_then':
                    with open("1", "w+") as ff:
                        ff.write(str(parsed))
                gen.Generator().late(parsed, f"{results_path}/{file_name}.go")
        except FileNotFoundError as e:
            if e.filename == f'{tests_path}/{file_name}.cpp':
                print(f'Файл {tests_path}/{file_name}.cpp не найден!')
                ind = False
            else:
                import os
                os.mkdir(results_path)

                importlib.reload(cpp_grammar)
                importlib.reload(gen)
                importlib.reload(ep)

                kek = ep.EarleyParser(ep.lex.CppLexAnalyzer(), cpp_grammar.set_cpp())
                parsed = None

        else:
            ind = False


if __name__ == '__main__':
    translator('main', 'test_result_parse', 'test_cases')
    translator('main', 'test_result_parse', 'test_cases')
