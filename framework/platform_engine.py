import os.path
from appium import webdriver
from framework.logger import Logger  #日志文件
import yaml
logger=Logger(logger="PlatformEngine").getlog()
class PlatformEngline(object):
    def appium_desired(self):
        with open(os.path.dirname(os.path.abspath("."))+'/config/config.yaml','r',encoding='utf-8') as file:
            data = yaml.load(file)
        desired_caps={}
        desired_caps['platformName']=data['platformName']
        desired_caps["platformVersion"]=data["platformVersion"]
        desired_caps["deviceName"]=data["deviceName"]
        desired_caps["sessionOverride"]=True
        apk_path=os.path.dirname(os.path.abspath("."))
        desired_caps["app"]=apk_path+"/app/znbwl.apk"       #应用程序包
        desired_caps["noReset"]=True
        desired_caps["appPackage"]=data["appPackage"]
        desired_caps["appActivity"]=data["appActivity"]
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        return self.driver
    def quit_browser(self):
        self.driver.quit()
        logger.info("关闭程序")


