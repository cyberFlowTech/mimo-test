from appium.webdriver.common.mobileby import MobileBy
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from PageObjct.element_page.login_page import LoginPage
from time import sleep


class LoginStep(LoginPage):

    '''登录步骤'''

    def login1(self, username, password):
        # 切换到账户登录
        self.click(self.el_account)
        # 输入账号
        self.input(self.el_username, username)
        # 点击登录测试环境（下一步）
        self.click(self.el_login)
        # 输入密码
        self.input(self.el_password, password)
        # 点击登录
        self.click(self.el_login)
        sleep(2)

    '''一键注册'''

    def single(self):
        # 点击一键注册
        self.click(self.el_single)
        # 点击跳过
        self.click(self.el_skip2)
        # 点击我知道了
        self.click(self.el_know)

    '''注册步骤'''

    def login2(self, username, password, name):
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
        # 输入用户名
        self.input(self.el_pname, name)
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
        # 点击完成
        self.click(self.el_done)
        # 点击全选部落按钮
        self.click(self.el_all)
        # 点击进入部落
        self.click(self.el_join)
        sleep(1)
        # 点击我知道了
        self.click(self.el_know)

    '''退出登录'''

    def logout(self):
        # 点击“我的”tab
        self.click(self.el_my)
        # 点击退出登录
        self.click(self.el_logout)
        # 二次确认弹窗点击确认
        self.click(self.el_popup_logout_yes)
        # 切换其他账号登录
        self.click(self.el_login_another)

    def switch_account_203(self):
        # # 聊天室返回
        # self.click(self.el_go_back)
        # element = self.driver.find_elements(By.XPATH,'//XCUIElementTypeStaticText[@name="取消"]')
        # if element:
        #     element[0].click()
        # else:
        #     pass
        # 搜索页面返回
        # self.click(self.el_search_goback)
        # 退出账号
        self.logout()
        # 登录账号
        self.login1('new203', 'Sta12345')

    def switch_account_202(self):
        # # 聊天室返回
        # self.click(self.el_go_back)
        # element = self.driver.find_elements(By.XPATH,'//XCUIElementTypeStaticText[@name="取消"]')
        # if element:
        #     element[0].click()
        # else:
        #     pass
        # 搜索页面返回
        # self.click(self.el_search_goback)
        # 退出账号
        self.logout()
        # 登录账号
        self.login1('new202', 'Sta12345')

    def account_is_202(self):
        try:
            # 使用显式等待定位元素
            element_my = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//XCUIElementTypeImage[@name="mine_unselected_icon_light"]'))
            )

            if element_my.is_displayed():
                element_my.click()

                try:
                    # 检查账号名是否显示
                    element_name = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(
                        (By.XPATH, '(//XCUIElementTypeStaticText[@name="new202"])[2]')))
                    self.click(el_club)
                    return True  # 已经是目标账号

                except TimeoutException:
                    print("未找到new202账号，正在切换...")
                    self.switch_account_202()
                    return True

        except TimeoutException:
            # 如果找不到个人资料图标，检查是否在登录页面
            if WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located(
                        (By.XPATH, '//XCUIElementTypeStaticText[@name="账号"]'))).is_displayed():
                self.login1('new202', 'Sta12345')
                return True

        except Exception as e:
            print(f"检查账号时出现意外错误: {str(e)}")
            return False
