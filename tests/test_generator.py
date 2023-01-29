import unittest
import sys
import os
import tempfile

sys.path.insert(1, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.code_generator.generator import Generator


class TestCodeGenerator(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.__temp_dir = tempfile.TemporaryDirectory()

    def setUp(self):
        self.__generator = Generator()

    def test_generator_type(self):
        value = [['int', 'R3', 1], ['main', 'ID', 1], ['(', 'D6', 1], [')', 'D7', 1], ['{', 'D4', 1],
                 ['bool', 'R1', 3], ['b1', 'ID', 3], [';', 'D3', 3], ['char', 'R2', 4], ['c1', 'ID', 4],
                 [';', 'D3', 4], ['int', 'R3', 5], ['i1', 'ID', 5], [';', 'D3', 5], ['float', 'R4', 6],
                 ['f1', 'ID', 6], [';', 'D3', 6], ['double', 'R5', 7], ['d1', 'ID', 7], [';', 'D3', 7],
                 ['bool', 'R1', 9], ['b2', 'ID', 9], ['=', 'O15', 9], ['true', 'R7', 9], [';', 'D3', 9],
                 ['char', 'R2', 10], ['c2', 'ID', 10], ['=', 'O15', 10], ["'c'", 'C', 10], [';', 'D3', 10],
                 ['int', 'R3', 11], ['i2', 'ID', 11], ['=', 'O15', 11], ['43', 'N', 11], [';', 'D3', 11],
                 ['float', 'R4', 12], ['f2', 'ID', 12], ['=', 'O15', 12], ['4', 'N', 12], ['.', 'D1', 12],
                 ['3', 'N', 12], [';', 'D3', 12], ['double', 'R5', 13], ['d2', 'ID', 13], ['=', 'O15', 13],
                 ['4', 'N', 13], ['.', 'D1', 13], ['3', 'N', 13], [';', 'D3', 13], ['return', 'K10', 15],
                 ['0', 'N', 15], [';', 'D3', 15], ['}', 'D5', 16]]

        self.__generator.late(value, f"{self.__temp_dir.name}/types.go")
        with open(f'{self.__temp_dir.name}/types.go', 'r') as f:
            result = f.read().replace("\r\n", "\n")
        with open('test_expected_parse/types.go', 'r') as f:
            expected = f.read().replace("\r\n", "\n")
        self.assertEqual(result, expected)

    def test_generator_operators(self):
        value = [['int', 'R3', 1], ['main', 'ID', 1], ['(', 'D6', 1], [')', 'D7', 1],
                 ['{', 'D4', 1], ['int', 'R3', 3], ['a', 'ID', 3], ['=', 'O15', 3],
                 ['10', 'N', 3], [';', 'D3', 3], ['int', 'R3', 4], ['b', 'ID', 4],
                 ['=', 'O15', 4], ['20', 'N', 4], [';', 'D3', 4], ['int', 'R3', 5],
                 ['c', 'ID', 5], ['=', 'O15', 5], ['0', 'N', 5], [';', 'D3', 5],
                 ['bool', 'R1', 6], ['too', 'ID', 6], ['=', 'O15', 6], ['true', 'R7', 6],
                 [';', 'D3', 6], ['bool', 'R1', 7], ['foo', 'ID', 7], ['=', 'O15', 7],
                 ['false', 'R8', 7], [';', 'D3', 7], ['bool', 'R1', 8], ['roo', 'ID', 8],
                 [';', 'D3', 8], ['c', 'ID', 10], ['=', 'O15', 10], ['a', 'ID', 10],
                 ['+', 'O1', 10], ['b', 'ID', 10], [';', 'D3', 10], ['c', 'ID', 11],
                 ['=', 'O15', 11], ['a', 'ID', 11], ['-', 'O2', 11], ['b', 'ID', 11],
                 [';', 'D3', 11], ['c', 'ID', 12], ['=', 'O15', 12], ['a', 'ID', 12],
                 ['*', 'O3', 12], ['b', 'ID', 12], [';', 'D3', 12], ['c', 'ID', 13],
                 ['=', 'O15', 13], ['a', 'ID', 13], ['/', 'O4', 13], ['b', 'ID', 13],
                 [';', 'D3', 13], ['c', 'ID', 14], ['=', 'O15', 14], ['a', 'ID', 14],
                 ['%', 'O5', 14], ['b', 'ID', 14], [';', 'D3', 14], ['roo', 'ID', 16],
                 ['=', 'O15', 16], ['!', 'O8', 16], ['foo', 'ID', 16], [';', 'D3', 16],
                 ['roo', 'ID', 17], ['=', 'O15', 17], ['too', 'ID', 17], ['||', 'O6', 17],
                 ['foo', 'ID', 17], [';', 'D3', 17], ['roo', 'ID', 18], ['=', 'O15', 18],
                 ['foo', 'ID', 18], ['&&', 'O7', 18], ['too', 'ID', 18], [';', 'D3', 18],
                 ['foo', 'ID', 20], ['=', 'O15', 20], ['a', 'ID', 20], ['>', 'O9', 20],
                 ['b', 'ID', 20], [';', 'D3', 20], ['foo', 'ID', 21], ['=', 'O15', 21],
                 ['a', 'ID', 21], ['<', 'O10', 21], ['b', 'ID', 21], [';', 'D3', 21],
                 ['foo', 'ID', 22], ['=', 'O15', 22], ['a', 'ID', 22], ['>=', 'O11', 22],
                 ['b', 'ID', 22], [';', 'D3', 22], ['foo', 'ID', 23], ['=', 'O15', 23],
                 ['a', 'ID', 23], ['<=', 'O12', 23], ['b', 'ID', 23], [';', 'D3', 23],
                 ['foo', 'ID', 24], ['=', 'O15', 24], ['a', 'ID', 24], ['==', 'O13', 24],
                 ['b', 'ID', 24], [';', 'D3', 24], ['foo', 'ID', 25], ['=', 'O15', 25],
                 ['a', 'ID', 25], ['!=', 'O14', 25], ['b', 'ID', 25], [';', 'D3', 25],
                 ['return', 'K10', 27], ['0', 'N', 27], [';', 'D3', 27], ['}', 'D5', 28]]

        self.__generator.late(value, f'{self.__temp_dir.name}/operators.go')
        with open(f'{self.__temp_dir.name}/operators.go', 'r') as f:
            result = f.read().replace("\r\n", "\n")
        with open('test_expected_parse/operators.go', 'r') as f:
            expected = f.read().replace("\r\n", "\n")
        self.assertEqual(result, expected)

    def test_generator_loops(self):
        value = [['int', 'R3', 1], ['main', 'ID', 1], ['(', 'D6', 1], [')', 'D7', 1], ['{', 'D4', 1],
                 ['int', 'R3', 2], ['c', 'ID', 2], ['=', 'O15', 2], ['10', 'N', 2], [';', 'D3', 2],
                 ['int', 'R3', 3], ['r', 'ID', 3], ['=', 'O15', 3], ['0', 'N', 3], [';', 'D3', 3],
                 ['for', 'K3', 5], ['(', 'D6', 5], ['int', 'R3', 5], ['i', 'ID', 5], ['=', 'O15', 5],
                 ['1', 'N', 5], [';', 'D3', 5], ['i', 'ID', 5], ['<=', 'O12', 5], ['5', 'N', 5],
                 [';', 'D3', 5], ['i', 'ID', 5], ['=', 'O15', 5], ['i', 'ID', 5], ['+', 'O1', 5],
                 ['1', 'N', 5], [')', 'D7', 5], ['{', 'D4', 5], ['r', 'ID', 6], ['=', 'O15', 6],
                 ['r', 'ID', 6], ['+', 'O1', 6], ['1', 'N', 6], [';', 'D3', 6], ['}', 'D5', 7],
                 ['while', 'K9', 9], ['(', 'D6', 9], ['r', 'ID', 9], ['<=', 'O12', 9], ['20', 'N', 9],
                 [')', 'D7', 9], ['{', 'D4', 9], ['r', 'ID', 10], ['=', 'O15', 10], ['r', 'ID', 10],
                 ['+', 'O1', 10], ['1', 'N', 10], [';', 'D3', 10], ['}', 'D5', 11], ['do', 'K1', 13],
                 ['{', 'D4', 13], ['r', 'ID', 14], ['=', 'O15', 14], ['r', 'ID', 14], ['+', 'O1', 14],
                 ['1', 'N', 14], [';', 'D3', 14], ['}', 'D5', 15], ['while', 'K9', 16], ['(', 'D6', 16],
                 ['r', 'ID', 16], ['<=', 'O12', 16], ['30', 'N', 16], [')', 'D7', 16], [';', 'D3', 16],
                 ['return', 'K10', 18], ['0', 'N', 18], [';', 'D3', 18], ['}', 'D5', 19]]

        self.__generator.late(value, f'{self.__temp_dir.name}/loops.go')
        with open(f'{self.__temp_dir.name}/loops.go', 'r') as f:
            result = f.read().replace("\r\n", "\n")
        with open('test_expected_parse/loops.go', 'r') as f:
            expected = f.read().replace("\r\n", "\n")
        self.assertEqual(result, expected)

    def test_generator_main(self):
        value = [['int', 'R3', 1], ['main', 'ID', 1], ['(', 'D6', 1], [')', 'D7', 1], ['{', 'D4', 1], ['int', 'R3', 2],
                 ['r', 'ID', 2], ['=', 'O15', 2], ['10', 'N', 2], [';', 'D3', 2], ['int', 'R3', 3], ['c', 'ID', 3],
                 ['=', 'O15', 3], ['10', 'N', 3], [';', 'D3', 3], ['int', 'R3', 4], ['r', 'ID', 4], ['=', 'O15', 4],
                 ['0', 'N', 4], [';', 'D3', 4], ['for', 'K3', 6], ['(', 'D6', 6], ['int', 'R3', 6], ['i', 'ID', 6],
                 ['=', 'O15', 6], ['1', 'N', 6], [';', 'D3', 6], ['i', 'ID', 6], ['<=', 'O12', 6], ['5', 'N', 6],
                 [';', 'D3', 6], ['i', 'ID', 6], ['=', 'O15', 6], ['i', 'ID', 6], ['+', 'O1', 6], ['1', 'N', 6],
                 [')', 'D7', 6], ['{', 'D4', 6], ['for', 'K3', 7], ['(', 'D6', 7], ['int', 'R3', 7], ['k', 'ID', 7],
                 ['=', 'O15', 7], ['5', 'N', 7], [';', 'D3', 7], ['k', 'ID', 7], ['<=', 'O12', 7], ['10', 'N', 7],
                 [';', 'D3', 7], ['k', 'ID', 7], ['=', 'O15', 7], ['k', 'ID', 7], ['+', 'O1', 7], ['2', 'N', 7],
                 [')', 'D7', 7], ['{', 'D4', 7], ['for', 'K3', 8], ['(', 'D6', 8], ['int', 'R3', 8], ['z', 'ID', 8],
                 ['=', 'O15', 8], ['1', 'N', 8], [';', 'D3', 8], ['z', 'ID', 8], ['<=', 'O12', 8], ['12', 'N', 8],
                 [';', 'D3', 8], ['z', 'ID', 8], ['=', 'O15', 8], ['z', 'ID', 8], ['+', 'O1', 8], ['1', 'N', 8],
                 [')', 'D7', 8], ['{', 'D4', 8], ['c', 'ID', 9], ['=', 'O15', 9], ['c', 'ID', 9], ['*', 'O3', 9],
                 ['5', 'N', 9], [';', 'D3', 9], ['}', 'D5', 10], ['c', 'ID', 11], ['=', 'O15', 11], ['c', 'ID', 11],
                 ['*', 'O3', 11], ['10', 'N', 11], [';', 'D3', 11], ['for', 'K3', 12], ['(', 'D6', 12],
                 ['int', 'R3', 12], ['z', 'ID', 12], ['=', 'O15', 12], ['1', 'N', 12], [';', 'D3', 12],
                 ['z', 'ID', 12], ['<=', 'O12', 12], ['12', 'N', 12], [';', 'D3', 12], ['z', 'ID', 12],
                 ['=', 'O15', 12], ['z', 'ID', 12], ['+', 'O1', 12], ['1', 'N', 12], [')', 'D7', 12],
                 ['{', 'D4', 12], ['c', 'ID', 13], ['=', 'O15', 13], ['c', 'ID', 13], ['*', 'O3', 13],
                 ['5', 'N', 13], [';', 'D3', 13], ['}', 'D5', 14], ['}', 'D5', 15], ['r', 'ID', 16],
                 ['=', 'O15', 16], ['r', 'ID', 16], ['+', 'O1', 16], ['1', 'N', 16], [';', 'D3', 16],
                 ['}', 'D5', 17], ['while', 'K9', 19], ['(', 'D6', 19], ['r', 'ID', 19], ['<=', 'O12', 19],
                 ['20', 'N', 19], [')', 'D7', 19], ['{', 'D4', 19], ['int', 'R3', 20], ['d', 'ID', 20],
                 ['=', 'O15', 20], ['10', 'N', 20], [';', 'D3', 20], ['while', 'K9', 21], ['(', 'D6', 21],
                 ['d', 'ID', 21], ['>=', 'O11', 21], ['5', 'N', 21], [')', 'D7', 21], ['{', 'D4', 21],
                 ['r', 'ID', 22], ['=', 'O15', 22], ['r', 'ID', 22], ['+', 'O1', 22], ['1', 'N', 22],
                 [';', 'D3', 22], ['}', 'D5', 23], ['r', 'ID', 24], ['=', 'O15', 24], ['r', 'ID', 24],
                 ['+', 'O1', 24], ['1', 'N', 24], [';', 'D3', 24], ['}', 'D5', 25], ['do', 'K1', 27],
                 ['{', 'D4', 27], ['r', 'ID', 28], ['=', 'O15', 28], ['r', 'ID', 28], ['+', 'O1', 28],
                 ['1', 'N', 28], [';', 'D3', 28], ['do', 'K1', 29], ['{', 'D4', 29], ['c', 'ID', 30],
                 ['=', 'O15', 30], ['c', 'ID', 30], ['+', 'O1', 30], ['20', 'N', 30], [';', 'D3', 30],
                 ['}', 'D5', 31], ['while', 'K9', 32], ['(', 'D6', 32], ['c', 'ID', 32], ['<=', 'O12', 32],
                 ['5000', 'N', 32], [')', 'D7', 32], [';', 'D3', 32], ['}', 'D5', 33], ['while', 'K9', 34],
                 ['(', 'D6', 34], ['r', 'ID', 34], ['<', 'O10', 34], ['100', 'N', 34], [')', 'D7', 34],
                 [';', 'D3', 34], ['return', 'K10', 36], ['0', 'N', 36], [';', 'D3', 36], ['}', 'D5', 37]]

        self.__generator.late(value, f'{self.__temp_dir.name}/main.go')
        with open(f'{self.__temp_dir.name}/main.go', 'r') as f:
            result = f.read().replace("\r\n", "\n")
        with open('test_expected_parse/main.go', 'r') as f:
            expected = f.read().replace("\r\n", "\n")
        self.assertEqual(result, expected)

    def test_generator_lextest(self):
        value = [['int', 'R3', 1], ['main', 'ID', 1], ['(', 'D6', 1], [')', 'D7', 1], ['{', 'D4', 1],
                 ['int', 'R3', 3], ['a', 'ID', 3], ['=', 'O15', 3], ['5', 'N', 3], [';', 'D3', 3],
                 ['float', 'R4', 4], ['b', 'ID', 4], ['=', 'O15', 4], ['4', 'N', 4], ['.', 'D1', 4],
                 ['5', 'N', 4], [';', 'D3', 4], ['bool', 'R1', 5], ['c', 'ID', 5], ['=', 'O15', 5],
                 ['a', 'ID', 5], ['<=', 'O12', 5], ['b', 'ID', 5], [';', 'D3', 5], ['return', 'K10', 6],
                 ['0', 'N', 6], [';', 'D3', 6], ['}', 'D5', 7]]

        self.__generator.late(value, f'{self.__temp_dir.name}/lextest.go')
        with open(f'{self.__temp_dir.name}/lextest.go', 'r') as f:
            result = f.read().replace("\r\n", "\n")
        with open('test_expected_parse/lextest.go', 'r') as f:
            expected = f.read().replace("\r\n", "\n")
        self.assertEqual(result, expected)

    def test_generator_if_then(self):
        value = [['int', 'R3', 1], ['main', 'ID', 1], ['(', 'D6', 1], [')', 'D7', 1], ['{', 'D4', 1],
                 ['int', 'R3', 2], ['a', 'ID', 2], ['=', 'O15', 2], ['1', 'N', 2], [';', 'D3', 2],
                 ['int', 'R3', 3], ['c', 'ID', 3], [';', 'D3', 3], ['if', 'K4', 5], ['(', 'D6', 5],
                 ['a', 'ID', 5], ['==', 'O13', 5], ['1', 'N', 5], [')', 'D7', 5], ['{', 'D4', 5],
                 ['c', 'ID', 6], ['=', 'O15', 6], ['0', 'N', 6], [';', 'D3', 6], ['}', 'D5', 7],
                 ['if', 'K4', 9], ['(', 'D6', 9], ['a', 'ID', 9], ['==', 'O13', 9], ['2', 'N', 9],
                 [')', 'D7', 9], ['{', 'D4', 9], ['c', 'ID', 10], ['=', 'O15', 10], ['1', 'N', 10],
                 [';', 'D3', 10], ['}', 'D5', 11], ['else', 'K2', 11], ['{', 'D4', 11], ['c', 'ID', 12],
                 ['=', 'O15', 12], ['2', 'N', 12], [';', 'D3', 12], ['}', 'D5', 13], ['if', 'K4', 15],
                 ['(', 'D6', 15], ['a', 'ID', 15], ['==', 'O13', 15], ['3', 'N', 15], [')', 'D7', 15],
                 ['{', 'D4', 15], ['c', 'ID', 16], ['=', 'O15', 16], ['3', 'N', 16], [';', 'D3', 16],
                 ['}', 'D5', 17], ['else', 'K2', 17], ['if', 'K4', 17], ['(', 'D6', 17], ['a', 'ID', 17],
                 ['==', 'O13', 17], ['4', 'N', 17], [')', 'D7', 17], ['{', 'D4', 17], ['c', 'ID', 18],
                 ['=', 'O15', 18], ['4', 'N', 18], [';', 'D3', 18], ['}', 'D5', 19], ['else', 'K2', 19],
                 ['{', 'D4', 19], ['c', 'ID', 20], ['=', 'O15', 20], ['5', 'N', 20], [';', 'D3', 20],
                 ['}', 'D5', 21], ['return', 'K10', 23], ['c', 'ID', 23], [';', 'D3', 23], ['}', 'D5', 24]]

        self.__generator.late(value, f'{self.__temp_dir.name}/if_then.go')
        with open(f'{self.__temp_dir.name}/if_then.go', 'r') as f:
            result = f.read().replace("\r\n", "\n")
        with open('test_expected_parse/if_then.go', 'r') as f:
            expected = f.read().replace("\r\n", "\n")
        self.assertEqual(result, expected)

    def test_generator_infernal_loops(self):
        value = [['int', 'R3', 1], ['main', 'ID', 1], ['(', 'D6', 1], [')', 'D7', 1], ['{', 'D4', 1],
                 ['int', 'R3', 2], ['c', 'ID', 2], ['=', 'O15', 2], ['10', 'N', 2], [';', 'D3', 2],
                 ['int', 'R3', 3], ['r', 'ID', 3], ['=', 'O15', 3], ['0', 'N', 3], [';', 'D3', 3],
                 ['for', 'K3', 5], ['(', 'D6', 5], ['int', 'R3', 5], ['i', 'ID', 5], ['=', 'O15', 5],
                 ['1', 'N', 5], [';', 'D3', 5], ['i', 'ID', 5], ['<=', 'O12', 5], ['5', 'N', 5],
                 [';', 'D3', 5], ['i', 'ID', 5], ['=', 'O15', 5], ['i', 'ID', 5], ['+', 'O1', 5],
                 ['1', 'N', 5], [')', 'D7', 5], ['{', 'D4', 5], ['for', 'K3', 6], ['(', 'D6', 6],
                 ['int', 'R3', 6], ['k', 'ID', 6], ['=', 'O15', 6], ['5', 'N', 6], [';', 'D3', 6],
                 ['k', 'ID', 6], ['<=', 'O12', 6], ['10', 'N', 6], [';', 'D3', 6], ['k', 'ID', 6],
                 ['=', 'O15', 6], ['k', 'ID', 6], ['+', 'O1', 6], ['2', 'N', 6], [')', 'D7', 6],
                 ['{', 'D4', 6], ['for', 'K3', 7], ['(', 'D6', 7], ['int', 'R3', 7], ['z', 'ID', 7],
                 ['=', 'O15', 7], ['1', 'N', 7], [';', 'D3', 7], ['z', 'ID', 7], ['<=', 'O12', 7],
                 ['12', 'N', 7], [';', 'D3', 7], ['z', 'ID', 7], ['=', 'O15', 7], ['z', 'ID', 7],
                 ['+', 'O1', 7], ['1', 'N', 7], [')', 'D7', 7], ['{', 'D4', 7], ['c', 'ID', 8],
                 ['=', 'O15', 8], ['c', 'ID', 8], ['*', 'O3', 8], ['5', 'N', 8], [';', 'D3', 8],
                 ['}', 'D5', 9], ['c', 'ID', 10], ['=', 'O15', 10], ['c', 'ID', 10], ['*', 'O3', 10],
                 ['10', 'N', 10], [';', 'D3', 10], ['for', 'K3', 11], ['(', 'D6', 11], ['int', 'R3', 11],
                 ['z', 'ID', 11], ['=', 'O15', 11], ['1', 'N', 11], [';', 'D3', 11], ['z', 'ID', 11],
                 ['<=', 'O12', 11], ['12', 'N', 11], [';', 'D3', 11], ['z', 'ID', 11], ['=', 'O15', 11],
                 ['z', 'ID', 11], ['+', 'O1', 11], ['1', 'N', 11], [')', 'D7', 11], ['{', 'D4', 11],
                 ['c', 'ID', 12], ['=', 'O15', 12], ['c', 'ID', 12], ['*', 'O3', 12], ['5', 'N', 12],
                 [';', 'D3', 12], ['}', 'D5', 13], ['}', 'D5', 14], ['r', 'ID', 15], ['=', 'O15', 15],
                 ['r', 'ID', 15], ['+', 'O1', 15], ['1', 'N', 15], [';', 'D3', 15], ['}', 'D5', 16],
                 ['while', 'K9', 18], ['(', 'D6', 18], ['r', 'ID', 18], ['<=', 'O12', 18], ['20', 'N', 18],
                 [')', 'D7', 18], ['{', 'D4', 18], ['int', 'R3', 19], ['d', 'ID', 19], ['=', 'O15', 19],
                 ['10', 'N', 19], [';', 'D3', 19], ['while', 'K9', 20], ['(', 'D6', 20], ['d', 'ID', 20],
                 ['>=', 'O11', 20], ['5', 'N', 20], [')', 'D7', 20], ['{', 'D4', 20], ['r', 'ID', 21],
                 ['=', 'O15', 21], ['r', 'ID', 21], ['+', 'O1', 21], ['1', 'N', 21], [';', 'D3', 21],
                 ['}', 'D5', 22], ['r', 'ID', 23], ['=', 'O15', 23], ['r', 'ID', 23], ['+', 'O1', 23],
                 ['1', 'N', 23], [';', 'D3', 23], ['}', 'D5', 24], ['do', 'K1', 26], ['{', 'D4', 26],
                 ['r', 'ID', 27], ['=', 'O15', 27], ['r', 'ID', 27], ['+', 'O1', 27], ['1', 'N', 27],
                 [';', 'D3', 27], ['do', 'K1', 28], ['{', 'D4', 28], ['c', 'ID', 29], ['=', 'O15', 29],
                 ['c', 'ID', 29], ['+', 'O1', 29], ['20', 'N', 29], [';', 'D3', 29], ['}', 'D5', 30],
                 ['while', 'K9', 31], ['(', 'D6', 31], ['c', 'ID', 31], ['<=', 'O12', 31], ['5000', 'N', 31],
                 [')', 'D7', 31], [';', 'D3', 31], ['}', 'D5', 32], ['while', 'K9', 33], ['(', 'D6', 33],
                 ['r', 'ID', 33], ['<=', 'O12', 33], ['30', 'N', 33], [')', 'D7', 33], [';', 'D3', 33],
                 ['return', 'K10', 35], ['0', 'N', 35], [';', 'D3', 35], ['}', 'D5', 36]]

        self.__generator.late(value, f'{self.__temp_dir.name}/infernal_loops.go')
        with open(f'{self.__temp_dir.name}/infernal_loops.go', 'r') as f:
            result = f.read().replace("\r\n", "\n")
        with open('test_expected_parse/infernal_loops.go', 'r') as f:
            expected = f.read().replace("\r\n", "\n")
        self.assertEqual(result, expected)
