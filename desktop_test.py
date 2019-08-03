from pages.desktops_page import DesktopOrder
from utilities.teststatus import ResultStatus
import pytest,unittest
from ddt import ddt,data,unpack
from utilities.read_data import getCSVData,readAndWrite

@pytest.mark.usefixtures("oneTimeSetUp")
@ddt
class DesktopOrderTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectsetup(self,oneTimeSetUp):
        self.dtop = DesktopOrder(self.driver)
        self.rs = ResultStatus(self.driver)

    # @pytest.mark.run(order=1)
    # @data(*getCSVData("/Users/Abilash/PycharmProjects/AT/sonyorderdata.csv"))
    @data(*readAndWrite("/Users/Abilash/PycharmProjects/AT/sonyorderdata.csv"))
    @unpack
    def test_desktop(self,FirstName,LastName,Address1,City,Postalcode):
        self.dtop.orderDesktop()
        res1 = self.dtop.verifydesktopadddedsuccessfully()
        self.rs.mark(result=res1,resultMessage='Added to cart')
        self.dtop.opencart(FirstName,LastName,Address1,City,Postalcode)
        result2 = self.dtop.verifyorderSuccessfull()
        self.rs.markFinal('Verifying the order placed successfully',result2,'Order Verification')

