import unittest

import xmlrunner
import sys



def creatsuite():
    print "Creating test suite"
    testunit = unittest.TestSuite()
    test_dir = 'D:/Calculation/test'
    discover = unittest.defaultTestLoader.discover(test_dir)
    for test_case in discover:
        print(test_case)
        testunit.addTests(test_case)
    return testunit


dest_path = "D:/Calculation"
runner = xmlrunner.XMLTestRunner(output=dest_path)

if __name__ == '__main__':
    print "Inside Main"
    alltestnames = creatsuite()
    result = runner.run(alltestnames)
    print result
    failures = len(result.failures)
    errors = len(result.errors)
    print "failures " + str(failures)
    print "errors " + str(errors)