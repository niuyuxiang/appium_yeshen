from pageobjects.yeshen_homepage import HomePage
from testsuite.base_testcase import BaseTestCase
import time
import unittest
class YeshenRank(BaseTestCase):
    def test_yeshen_login(self):   #一定要test开头，把测试逻辑代码封装到一个test开头的方法里
        home_page=HomePage(self.driver)
        time.sleep(5)
        home_page.rank()
        time.sleep(5)
if __name__=="__main__":
    unittest.main()