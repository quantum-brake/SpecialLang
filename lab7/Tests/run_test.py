import coverage
import unittest

def main():
    # Start coverage
    cov = coverage.Coverage()
    cov.start()

    # Discover and run tests
    loader = unittest.TestLoader()
    suite = loader.discover('.')  # Changed to current directory to discover all tests
    unittest.TextTestRunner().run(suite)

    # Stop coverage and save report
    cov.stop()
    cov.save()
    cov.report()
    cov.html_report(directory='coverage_html_report')

if __name__ == '__main__':
    main()