from time import sleep
from tkinter.font import names

from appium.webdriver.common.mobileby import MobileBy
from Base.base_page import BasePage


class LoginPage(BasePage):

    #账号tab
    el_account = (MobileBy.ACCESSIBILITY_ID,"账号")
    #账户输入框
    el_username = (MobileBy.CLASS_NAME,'XCUIElementTypeTextField')
    #密码输入框
    el_password = (MobileBy.XPATH,'//XCUIElementTypeApplication[@name="Zapry"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther')
    #登录按钮
    el_login = (MobileBy.XPATH,'//XCUIElementTypeButton[@name="登录测试环境"]')
    #下一步
    el_nex = (MobileBy.XPATH,'//XCUIElementTypeButton[@name="下一步"]')
    #一键注册按钮
    el_single = (MobileBy.XPATH,'//XCUIElementTypeButton[@name="一键注册"]')
    #新注册用户页面的跳过
    el_skip2 = (MobileBy.XPATH,'//XCUIElementTypeStaticText[@name="跳过"]')
    #全选部落
    el_all = (MobileBy.XPATH,'//XCUIElementTypeButton[@name="全选"]')
    #进入部落按钮
    el_join = (MobileBy.ACCESSIBILITY_ID,'进入部落')
    #我知道了
    el_know = (MobileBy.XPATH,'//XCUIElementTypeButton[@name="我知道了"]')
    # 设置头像
    el_heads = (MobileBy.XPATH,'//XCUIElementTypeApplication[@name="Zapry"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeButton[1]')
    # 选择图片
    el_photo = (MobileBy.XPATH,'//XCUIElementTypeApplication[@name="Zapry"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[8]/XCUIElementTypeOther/XCUIElementTypeImage')
    # 完成
    el_done1 = (MobileBy.XPATH,'(//XCUIElementTypeStaticText[@name="完成"])[2]')
    #裁剪完成
    el_tailor = (MobileBy.XPATH,'//XCUIElementTypeStaticText[@name="完成"]')
    #输入名字
    el_pname = (MobileBy.CLASS_NAME,'XCUIElementTypeTextField')
    #点击完成
    el_done = (MobileBy.XPATH,'//XCUIElementTypeButton[@name="完成"]')


    #登录步骤
    def login1(self,username,password):
        #切换到账户登录
        self.click(self.el_account)
        #输入账号
        self.input(self.el_username,username)
        #点击登录测试环境（下一步）
        self.click(self.el_login)
        #输入密码
        self.input(self.el_password,password)
        #点击登录
        self.click(self.el_login)
        sleep(2)

    #一键注册
    def single(self):
        #点击一键注册
        self.click(self.el_single)
        # 点击跳过
        self.click(self.el_skip2)
        # 点击我知道了
        self.click(self.el_know)


        #注册步骤
    def login2(self,username,password,name):
        # 切换到账户登录
        self.click(self.el_account)
        # 输入账号
        self.input(self.el_username, username)
        # 点击登录测试环境（下一步）
        self.click(self.el_login)
        # 输入密码
        self.input(self.el_password, password)
        # 点击登录
        self.click(self.el_nex)
        #输入用户名
        self.input(self.el_pname,name)
        # 点击设置头像
        self.click(self.el_heads)
        # 选择照片
        self.click(self.el_photo)
        # 点击完成
        self.click(self.el_done1)
        # 太快了找不到元素
        sleep(1)
        # 裁剪完成
        self.click(self.el_tailor)
        #点击完成
        self.click(self.el_done)
        # 点击全选部落按钮
        self.click(self.el_all)
        # 点击进入部落
        self.click(self.el_join)
        sleep(1)
        # 点击我知道了
        self.click(self.el_know)