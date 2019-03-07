import unittest
from testsuite.base_testcase import BaseTestCase
from pageobjects.yeshen_homepage import HomePage
from framework.util import Util
from ddt import *
import time
testdata=Util.read_excel("E:\\appium_yeshen\data\excel.xlsx","Sheet1")
@ddt
class Login(BaseTestCase):
    @data(*testdata)
    def test_login(self,data):
        time.sleep(5)
        username=data["username"]#键
        print("搜索内容->：%s" %username) #值
        pwd=data["pwd"]
        print("搜索内容->：%s" %pwd)
        homepage=HomePage(self.driver)  #实例化homepage
        homepage.login(username,pwd)  #调用实例化中的login方法
        homepage.quit_login()   #退出登录
if __name__=='__main__':
    unittest.main()