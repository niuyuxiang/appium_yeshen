import testsuite
from pageobjects.yeshen_homepage import HomePage
from testsuite.base_testcase import BaseTestCase
import time
import unittest
class YeshenRegister(BaseTestCase):
    def test_yeshen_seach(self):   #一定要test开头，把测试逻辑代码封装到一个test开头的方法里
        home_page=HomePage(self.driver)
        time.sleep(10)#声明HomePage类对象
        home_page.search("nyx","3032988695@qq.com","123456nyx")  #调用首页搜索功能
        time.sleep(10)
if __name__=="__main__":
    unittest.main()
