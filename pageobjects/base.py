from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.logger import Logger
import time
import os.path

logger=Logger(logger='BasePage').getlog()
class BasePage(object):
    def __init__(self,driver):
        self.driver=driver

    def click(self,*loc):
        el = self.find_element(*loc)
        try:
            el.click()
            logger.info("已成功被点击")
        except Exception as e:
            logger.error("点击失败%s"%e)

    def click_someone(self,num,*loc):
        el=self.driver.find_elements(*loc)
        try:
            el[num].click()
            logger.info("成功被点击")
        except Exception as e:
            logger.error("点击失败%s"%e)

    def send_keys(self, text, *loc):
        el=self.find_element(*loc)
        el.clear()
        try:
            el.send_keys(text)
            logger.info("%s被输入" %text)
        except Exception as e:
            logger.error("Failed to type in input box with %s"%(el).text)
            self.get_windows_img()

    def gettext(self,*loc):
        el=self.find_element(*loc)
        text=el.text
        logger.info("你已经成功获取到文本：%s"%(el).text)
        return text

    def clear(self,*loc):
        el=self.find_element(*loc)
        try:
            el.clear()
            logger.info("已经清楚了文本框内容")
        except Exception as e:
            logger.error("clear fail%s"%e)

    def resetAPP(self):
        self.driver.resetApp()

    def find_element(self, *loc):
        try:
            WebDriverWait(self.driver,5).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except Exception as e:
            logger.error("find element%s"%e)

    def find_elements(self,*loc):
        try:
            WebDriverWait(self.driver,5).until(EC.visibility_of_element_located(loc))
            return self.driver.find_elements(*loc)
        except Exception as e:
            logger.error("find elements%s"%e)

    def get_windows_img(self):  #截图
        file_path=os.path.dirname(os.path.abspath('.'))+'/screenshots/'  #找文件夹
        if not os.path.exists(file_path):
            os.mkdir(file_path)  #创建文件夹
        rq=time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
        screen_name=file_path + rq + '.png'   #图片保存格式
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info('截图保存到 /screenshots')
        except Exception as e:
            self.get_windows_img()
            logger.error('获取截图失败，因为%s'%e)

    def slide(self,a,b,c,d,time):  #窗口滑动
        # print(self.driver.get_window_size())
        # x = self.driver.get_window_size()['width']  # # 获取屏幕的高
        # y = self.driver.get_window_size()['height']  # # 获取屏幕宽
        self.driver.swipe(a,b,c,d, time)   #a,b要移动的x,y    c,d将要移动的x,y    time长按时间
        # time.sleep(4)




