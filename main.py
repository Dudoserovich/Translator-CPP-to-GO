import config

if __name__ == '__main__':
    import sys
    from translator import translator

    if len(sys.argv) > 1:
        filename = sys.argv[1]
        translator(filename, config.RESULTS_PATH, "./")
    else:
        filename = 'main'
        translator(filename, config.RESULTS_PATH, config.TESTS_PATH)


