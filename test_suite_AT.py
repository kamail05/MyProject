import unittest
from tests.desktop_test import DesktopOrderTest
from tests.apple_test import AppleOrderTest

# Creating testcase by getting all tests from test  classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(DesktopOrderTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(AppleOrderTest)

# Creating test suite by combining all tests
smokeTest = unittest.TestSuite([tc1,tc2])

unittest.TextTestRunner(verbosity=2).run(smokeTest)

