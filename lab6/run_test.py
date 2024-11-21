import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import coverage
import unittest

def main():
    # Start coverage
    cov = coverage.Coverage()
    cov.start()

    # Discover and run tests
    loader = unittest.TestLoader()
    suite = loader.discover(os.path.dirname(__file__), pattern='test_*.py')
    result = unittest.TextTestRunner(verbosity=2).run(suite)

    # Stop coverage and save report
    cov.stop()

    # Якщо тестів не було виконано
    if not result.testsRun:
        print("Увага: Жодних тестів не було виконано.")
    else:
        cov.save()
        cov.report()
        cov.html_report(directory='coverage_html_report')

if __name__ == '__main__':
    main()
