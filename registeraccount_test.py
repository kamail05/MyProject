from pages.accountRegisterPage import RegisterAccount
from utilities.teststatus import ResultStatus
import unittest,pytest
from ddt import ddt,data,unpack
from utilities.read_data import getCSVData,readAndWrite

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class AccountRegisterTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectsetup(self,oneTimeSetUp):
        self.account = RegisterAccount(self.driver)
        self.ts = ResultStatus(self.driver)

    @data(*getCSVData("/Users/Abilash/PycharmProjects/AT/accountdata.csv"))
    # @data(*readAndWrite("/Users/Abilash/PycharmProjects/AT/accountdata.csv"))
    @unpack
    def test_registerAccount(self,FName,LName,Email,Teleophone,Password,ConfirmPassword):
        self.account.registerAccount(FName,LName,Email,Teleophone,Password,ConfirmPassword)
        result = self.account.verifyaccountCreatedSuccessfully()
        self.ts.markFinal("New Account Creation",result,"Successfull")


