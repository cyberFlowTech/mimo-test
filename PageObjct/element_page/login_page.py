from time import sleep
from tkinter.font import names

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

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
    '''我的tab'''
    # 底部“我的”tab
    el_my = MobileBy.ACCESSIBILITY_ID, 'mine_unselected_icon_light'
    # el_my = By.XPATH,'//XCUIElementTypeImage[@name="mine_unselected_icon_light"]'
    # 退出登录
    el_logout = MobileBy.XPATH, '(//XCUIElementTypeButton[@name="退出登录"])[2]'
    # 退出登录二次确认
    el_popup_logout_yes = MobileBy.XPATH, '//XCUIElementTypeButton[@name="确定"]'
    # 登录其他账号
    el_login_another = MobileBy.XPATH,'//XCUIElementTypeStaticText[@name="登录其他账号"]'
    '''聊天室'''
    # 返回
    el_go_back = MobileBy.ACCESSIBILITY_ID, '返回'
    # 搜索返回
    el_search_goback = MobileBy.XPATH,'//XCUIElementTypeStaticText[@name="取消"]'