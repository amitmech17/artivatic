import unittest
from tests.Checkout.Checkout_tests import CheckoutFlowTests
from tests.ApiTask.Api_tests import ApiTests
# from tests.courses.register_courses_csv_data import RegisterCoursesCSVDataTests

# Get all tests from the test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(CheckoutFlowTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(ApiTests)


# Create a test suite combining all test classes
smokeTest = unittest.TestSuite([tc1,tc2])

unittest.TextTestRunner(verbosity=2).run(smokeTest)