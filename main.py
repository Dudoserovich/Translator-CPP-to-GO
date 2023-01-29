import os
import sys
import config

from src.translator import translator


if __name__ == '__main__':
    for root, dirs, files in os.walk(config.TESTS_PATH):
        for filename in files:
            print(filename.replace('.cpp', ''))
    filename = sys.argv[1] if len(sys.argv) > 1 else 'main'
    translator("operators", config.RESULTS_PATH, config.TESTS_PATH)
