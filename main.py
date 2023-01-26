import config

if __name__ == '__main__':
    import sys
    from translator import translator

    filename = sys.argv[1] if len(sys.argv) > 1 else 'main'

    translator(filename, config.RESULTS_PATH, config.TESTS_PATH)
    translator(filename, config.RESULTS_PATH, config.TESTS_PATH)
