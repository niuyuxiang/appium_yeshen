import sys
sys.path.append("E:\\appium_yeshen")

import unittest
import HTMLTestRunner
import os
from testsuite.test_yeshen_register import YeshenRegister
from testsuite.test_yeshen_login import YeshenLogin
from testsuite.test_yeshen_alter import YeshenAlter
from testsuite.test_yeshen_add import YeshenAdd
from testsuite.test_yeshen_seek import YeshenSeek
from testsuite.test_yeshen_rank import YeshenRank
from testsuite.test_yeshen_file import YeshenPress
from testsuite.test_yeshen_delete import YeshenDelete
file_path=os.path.dirname(os.path.abspath("."))+"/test_report"
report_path=os.path.join(file_path,"report")
if not os.path.exists(report_path):
    os.mkdir(report_path)

suite=unittest.TestSuite()
suite.addTest(unittest.makeSuite(YeshenRegister))
suite.addTest(unittest.makeSuite(YeshenLogin))
suite.addTest(unittest.makeSuite(YeshenAlter))
suite.addTest(unittest.makeSuite(YeshenAdd))
suite.addTest(unittest.makeSuite(YeshenSeek))
suite.addTest(unittest.makeSuite(YeshenPress))
suite.addTest(unittest.makeSuite(YeshenRank))
suite.addTest(unittest.makeSuite(YeshenDelete))

if __name__=="__main__":
    html_report=report_path+r"\result.html"
    fp=open(html_report,"wb")
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,verbosity=2,title="单元测试报告",description="关于abs和sort的测试报告")
    runner.run(suite)