import unittest



import src.translator as translator
import config


class TestIntegration(unittest.TestCase):
    def test_main(self):
        file_name = 'main'
        translator.translator(file_name, config.RESULTS_PATH, config.TESTS_PATH)

        with open(f'{config.RESULTS_PATH}/{file_name}.go', 'r') as f:
            result = f.read().replace("\r\n", "\n")
        with open(f'{config.EXPECTED_PATH}/{file_name}.go', 'r') as f:
            expected = f.read().replace("\r\n", "\n")
        self.assertEqual(result, expected)

    def test_if_then(self):
        file_name = 'if_then'
        translator.translator(file_name, config.RESULTS_PATH, config.TESTS_PATH)

        with open(f'{config.RESULTS_PATH}/{file_name}.go', 'r') as f:
            result = f.read().replace("\r\n", "\n")
        with open(f'{config.EXPECTED_PATH}/{file_name}.go', 'r') as f:
            expected = f.read().replace("\r\n", "\n")
        self.assertEqual(result, expected)

    def test_infernal_loops(self):
        file_name = 'infernal_loops'
        translator.translator(file_name, config.RESULTS_PATH, config.TESTS_PATH)

        with open(f'{config.RESULTS_PATH}/{file_name}.go', 'r') as f:
            result = f.read().replace("\r\n", "\n")
        with open(f'{config.EXPECTED_PATH}/{file_name}.go', 'r') as f:
            expected = f.read().replace("\r\n", "\n")
        self.assertEqual(result, expected)

    def test_loops(self):
        file_name = 'loops'
        translator.translator(file_name, config.RESULTS_PATH, config.TESTS_PATH)

        with open(f'{config.RESULTS_PATH}/{file_name}.go', 'r') as f:
            result = f.read().replace("\r\n", "\n")
        with open(f'{config.EXPECTED_PATH}/{file_name}.go', 'r') as f:
            expected = f.read().replace("\r\n", "\n")
        self.assertEqual(result, expected)

    def test_lex(self):
        file_name = 'lextest'
        translator.translator(file_name, config.RESULTS_PATH, config.TESTS_PATH)

        with open(f'{config.RESULTS_PATH}/{file_name}.go', 'r') as f:
            result = f.read().replace("\r\n", "\n")
        with open(f'{config.EXPECTED_PATH}/{file_name}.go', 'r') as f:
            expected = f.read().replace("\r\n", "\n")
        self.assertEqual(result, expected)

    def test_operators(self):
        file_name = 'operators'
        translator.translator(file_name, config.RESULTS_PATH, config.TESTS_PATH)

        with open(f'{config.RESULTS_PATH}/{file_name}.go', 'r') as f:
            result = f.read().replace("\r\n", "\n")
        with open(f'{config.EXPECTED_PATH}/{file_name}.go', 'r') as f:
            expected = f.read().replace("\r\n", "\n")
        self.assertEqual(result, expected)

    def test_types(self):
        file_name = 'types'
        translator.translator(file_name, config.RESULTS_PATH, config.TESTS_PATH)

        with open(f'{config.RESULTS_PATH}/{file_name}.go', 'r') as f:
            result = f.read().replace("\r\n", "\n")
        with open(f'{config.EXPECTED_PATH}/{file_name}.go', 'r') as f:
            expected = f.read().replace("\r\n", "\n")
        self.assertEqual(result, expected)
