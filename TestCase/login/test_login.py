import os
import secrets
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

from Base.app_assert_page import AppAssertPage
from PageObjct.element_page.login_page import LoginPage
from common.data_util import readYaml


class TestLogin:

    def setup(self):
        # 回到根目录
        rootpath = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
        # yaml文件的绝对路径
        path = os.path.join(rootpath, 'config/config.yaml')
        # 拿到数据
        data = readYaml(path)
        # 连接Appium Server，初始化自动化环境
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', data['ios_caps'])

    def teardown(self):
        self.driver.quit()

    # @pytest.mark.parametrize('username,password', readYaml('../config/config.yaml'))
    def test_login1(self):
        login_page = LoginPage(driver=self.driver)
        '''账号登录'''
        login_page.login1('new203', 'Sta12345')
        sleep(1)
        ass = AppAssertPage(driver=self.driver)
        assert ass.is_element_present(MobileBy.ACCESSIBILITY_ID, 'tribe_add_light') == True

    def test_login2(self):
        login_page = LoginPage(driver=self.driver)
        '''新用户注册'''
        # 生成一个随机的令牌，例如用于安全令牌或密码
        token = secrets.token_hex(2)  # 生成一个2字节的十六进制字符串,4位
        data = 'new'
        ddname = data + token
        login_page.login2(ddname, 'Sta12345', '新注册用户')
        sleep(1)
        # 断言
        ass = AppAssertPage(driver=self.driver)
        assert ass.is_element_present(MobileBy.ACCESSIBILITY_ID, '参与共建热门部落') == True

    def test_single(self):
        login_page = LoginPage(driver=self.driver)
        '''一键注册'''
        login_page.single()
        sleep(1)
        ass = AppAssertPage(driver=self.driver)
        assert ass.is_element_present(MobileBy.ACCESSIBILITY_ID, '参与共建热门部落') == True
