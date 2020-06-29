#https://github.com/oldani/HtmlTestRunner

from unittest import TestLoader, TestSuite
from HtmlTestRunner import HTMLTestRunner
from config.conf import setup_env

from tests.tests_precondition import TestPrecondition
from tests.tests_postcondition import TestPostcondition
from tests.tests_login import TestLogin
#import tests_1
#import tests_2

setup_env('dev')

tests_precondition = TestLoader().loadTestsFromTestCase(TestPrecondition)
tests_postcondition = TestLoader().loadTestsFromTestCase(TestPostcondition)
tests_login = TestLoader().loadTestsFromTestCase(TestLogin)
#tests_1 = TestLoader().loadTestsFromTestCase(tests_1.ExampleTest1)
#tests_2 = TestLoader().loadTestsFromTestCase(tests_2.ExampleTest2)

suite = TestSuite([
    tests_precondition,
    tests_login,
    #tests_1, 
    #tests_2,
    tests_postcondition
    ])

runner = HTMLTestRunner(
    output=r'C:\test1',
    report_name="Test-Report",
    combine_reports=True
    )

runner.run(suite)
