from pageobjects.base import BasePage
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.touch_actions import TouchActions
import time
class HomePage(BasePage):
    ab_icon_button=(MobileBy.ID,"com.pdswp.su.smartcalendar:id/ab_icon")   #点击进入管理中心
    click_register_button=(MobileBy.ID,"com.pdswp.su.smartcalendar:id/email")  #点击注册备忘录平台
    login_button=(MobileBy.ID,"com.pdswp.su.smartcalendar:id/register")  #注册一个吧
    register_username=(MobileBy.ID,"com.pdswp.su.smartcalendar:id/username")   #昵称
    register_email=(MobileBy.ID,"com.pdswp.su.smartcalendar:id/email")  #注册邮箱
    register_password=(MobileBy.ID,"com.pdswp.su.smartcalendar:id/password")  #大于6位密码
    register_button=(MobileBy.ID,"com.pdswp.su.smartcalendar:id/reguser")    #注册

    click_login_button=(MobileBy.ID,"com.pdswp.su.smartcalendar:id/username")  #点击未登录
    login_email=(MobileBy.ID,"com.pdswp.su.smartcalendar:id/email")   #登录邮箱
    login_password=(MobileBy.ID,"com.pdswp.su.smartcalendar:id/password")  #登录密码
    login_button1=(MobileBy.ID,"com.pdswp.su.smartcalendar:id/login")  #点击登录
    quit_button=(MobileBy.ID,"com.pdswp.su.smartcalendar:id/exit")  #点击退出用户登录

    amend_username=(MobileBy.ID,"com.pdswp.su.smartcalendar:id/username")   #点击已经登录的用户名
    amend_title=(MobileBy.ID,"com.pdswp.su.smartcalendar:id/title")   #点击用户信息
    amend_username_after=(MobileBy.ID,"com.pdswp.su.smartcalendar:id/username")  #修改用户名
    amend_save=(MobileBy.ID,"com.pdswp.su.smartcalendar:id/quick_add")   #点击保存修改名

    menuAdd=(MobileBy.ID,"com.pdswp.su.smartcalendar:id/menuAdd")  #点击添加备忘录
    menuAdd_input=(MobileBy.ID,"com.pdswp.su.smartcalendar:id/add_input_content") #进入备忘录
    menuAdd_button=(MobileBy.ID,"com.pdswp.su.smartcalendar:id/quick_add")  #保存备忘录内容

    menuAdd2=(MobileBy.ID,"com.pdswp.su.smartcalendar:id/design_menu_item_text")  #复杂添加备忘录

    search_menu=(MobileBy.ID,"com.pdswp.su.smartcalendar:id/toolbar_search")  #点击搜索框
    search_borde=(MobileBy.ID,"android:id/search_src_text")  #点击搜索框的内容
    search_borde_content=(MobileBy.ID,"com.pdswp.su.smartcalendar:id/note_title")  #搜索框内的内容

    rank_button=(MobileBy.ID,'com.pdswp.su.smartcalendar:id/menu_sort')  #点击排序
    rank_save_button=(MobileBy.ID,"com.pdswp.su.smartcalendar:id/toolbar_ok")  #点击排序保存

    file=(MobileBy.ID,"com.pdswp.su.smartcalendar:id/menu_archive")   #把备忘录归档

    look_documents=(MobileBy.ID,"com.pdswp.su.smartcalendar:id/design_menu_item_text")  #查看归档
    return_documents=(MobileBy.ID,'com.pdswp.su.smartcalendar:id/menu')  #还原备忘录

    delete_memo=(MobileBy.ID,"com.pdswp.su.smartcalendar:id/menu_delete") #点击删除备忘录
    clear_recycle=(MobileBy.ID,"com.pdswp.su.smartcalendar:id/button")   #点击清空回收站
    ensure_button=(MobileBy.NAME,"确定")   #点击确定清空回收站

    def search(self,text1,text2,text3):  #用户注册
        self.click(*self.ab_icon_button)
        self.click(*self.click_register_button)
        self.click(*self.login_button)
        self.send_keys(text1,*self.register_username)
        self.send_keys(text2,*self.register_email)
        self.send_keys(text3,*self.register_password)
        self.click(*self.register_button)
        self.get_windows_img()

    def login(self,text4,text5): #用户登录
        self.click(*self.ab_icon_button)
        self.click(*self.click_login_button)
        self.send_keys(text4,*self.login_email)
        self.send_keys(text5,*self.login_password)
        self.click(*self.login_button1)
        self.get_windows_img()

    def quit_login(self):  #用户退出
        self.click(*self.ab_icon_button)
        self.click(*self.click_login_button)
        self.click(*self.quit_button)
        self.get_windows_img()

    def amend(self,text6):   #修改用户名
        self.click(*self.ab_icon_button)
        self.click(*self.amend_username)
        self.click(*self.amend_title)
        self.click(*self.amend_username_after)
        self.send_keys(text6,*self.amend_username_after)
        self.click(*self.amend_save)
        self.get_windows_img()

    def addmenu(self,text7):   #添加备忘录1
        self.click(*self.menuAdd)
        self.click(*self.menuAdd_input)
        self.send_keys(text7,*self.menuAdd_input)
        self.click(*self.menuAdd_button)
        self.get_windows_img()

    def addmenu2(self,text8):   #添加备忘录2
        self.click(*self.ab_icon_button)
        self.click(*self.menuAdd2)
        self.click(*self.menuAdd_input)
        self.send_keys(text8,*self.menuAdd_input)
        self.click(*self.menuAdd_button)
        self.get_windows_img()

    def search1(self,text9):   #搜索
        self.click(*self.search_menu)
        self.click(*self.search_borde)
        self.send_keys(text9,*self.search_borde)
        self.driver.keyevent(66)    #键盘回车
        self.get_windows_img()
    def yanzheng(self):  #验证搜索内容是否正确
        text11=self.gettext(*self.search_borde_content)
        return text11


    def rank(self): #排序
        action=TouchActions(self.driver)
        rank_word=self.driver.find_element_by_id("com.pdswp.su.smartcalendar:id/note_title")
        action.long_press(rank_word).perform()
        self.click(*self.rank_button)
        time.sleep(5)
        self.slide(681,159,683,268,500)
        self.click(*self.rank_save_button)
        self.get_windows_img()

    def press(self):   #长时间按压
        action=TouchActions(self.driver)
        look_word=self.driver.find_element_by_id("com.pdswp.su.smartcalendar:id/note_title")
        action.long_press(look_word).perform()
        self.get_windows_img()
        self.click(*self.file)


    def look(self,num):  #查看归档
        self.click(*self.ab_icon_button)
        time.sleep(5)
        self.click_someone(num,*self.look_documents)
        time.sleep(6)
        self.slide(412,127,102,127,500)
        self.click(*self.return_documents)
        self.get_windows_img()


    def delete(self):  #删除备忘录
        action=TouchActions(self.driver)
        look_word=self.driver.find_element_by_id("com.pdswp.su.smartcalendar:id/note_title")
        action.long_press(look_word).perform()
        self.click(*self.delete_memo)
        self.get_windows_img()

    def look_memo(self,text10):  #查看删除的备忘录
        self.click(*self.ab_icon_button)
        time.sleep(5)
        self.click_someone(text10,*self.look_documents)
        self.click(*self.clear_recycle)     #清空回收站
        self.get_windows_img()
        self.click(*self.ensure_button)








