import fnmatch
import os
import sys

import src.analyzers.lexical_analyzer as lex
import src.cpp_grammar as cpp_grammar
from src.code_generator.generator import *
from src.parser.earley_parser import *

# Поиск файла передаваемого транслятору
# по дефолту, если не переданы никакие аргументы, транслятору будет передан файл main.cpp
dirname_tests = 'test_cases'

filename = sys.argv[1] if len(sys.argv) > 1 else 'main'
listOfFiles = os.listdir(f'./{dirname_tests}')
pattern = f"{filename}.cpp"
check_search = False

for entry in listOfFiles:
    if fnmatch.fnmatch(entry, pattern):
        check_search = True

if not check_search:
    print('Файл не найден!')
    sys.exit()

# Инициализация всего необходимого
Gen = Generator()
myParser = EarleyParser(lex.CppLexAnalyzer(), cpp_grammar.set_cpp())

# Парсинг
f = open(f'{dirname_tests}/{filename}.cpp', 'r')
parsed = myParser.parse(f)
print(f"parse result:\n{parsed}")

# Генерация кода
Gen.late(parsed, filename)

f.close()
