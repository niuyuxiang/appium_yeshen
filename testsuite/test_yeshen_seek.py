from pageobjects.yeshen_homepage import HomePage
from testsuite.base_testcase import BaseTestCase
import time
import unittest
from ddt import ddt,data,unpack
@ddt
class YeshenSeek(BaseTestCase):
    @unpack
    def test_yeshen_login(self):   #一定要test开头，把测试逻辑代码封装到一个test开头的方法里
        home_page=HomePage(self.driver)
        time.sleep(3)
        home_page.search1("sou")
        print(home_page.yanzheng())
        try:
            self.assertEqual(home_page.yanzheng(),'sou',msg=home_page.yanzheng())
            print('验证正确')
        except:
            print('验证错误')
        time.sleep(10)
if __name__=="__main__":
    unittest.main()