from framework.platform_engine import PlatformEngline
import unittest
import warnings
class BaseTestCase(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        self.PlatformEngline=PlatformEngline()
        self.driver=self.PlatformEngline.appium_desired()
    def tearDown(self):
        print("测试结束")
        self.driver=self.PlatformEngline.quit_browser()