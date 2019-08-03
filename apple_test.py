from pages.appleorder_page import AppleOrder
import unittest,pytest
from utilities.teststatus import ResultStatus
from utilities.read_data import getCSVData
from ddt import ddt,data,unpack

@pytest.mark.usefixtures('oneTimeSetUp')
class AppleOrderTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectsetup(self):
        self.ao = AppleOrder(self.driver)
        self.ts = ResultStatus(self.driver)

    def test_appleorder(self):
        self.ao.orderapple()
        self.ao.verifyapplesuccessfully()
        result = self.ao.verifyapplesuccessfully()
        self.ts.markFinal("Testing Apple Order",result,'Verify order successfully added')
