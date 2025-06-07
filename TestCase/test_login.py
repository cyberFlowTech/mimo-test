
import secrets
from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from Base.app_assert_page import AppAssertPage
from PageObjct.operation_page.login_step import LoginStep
from common.start_app import start_app

class TestLogin:

    '''账号登录'''

    # @pytest.mark.parametrize('username,password', readYaml('../config/config.yaml'))
    def test_login_202(self,start_app):
        self.driver = start_app
        step = LoginStep(driver=self.driver)
        step.login1('new202', 'Sta12345')
        ass = AppAssertPage(self.driver)
        # 底部“部落”tab
        el = 'tribe_unselected_icon_light'
        assert ass.is_element_present(MobileBy.ACCESSIBILITY_ID, el) == True,f'未找到元素{el}，测试失败'

    '''新用户注册'''

    def test_login2(self,start_app):
        self.driver = start_app
        step = LoginStep(self.driver)
        # 生成一个随机的令牌，例如用于安全令牌或密码
        token = secrets.token_hex(2)  # 生成一个2个字节的十六进制字符串,4位
        data = 'new'
        use_name = data + token
        step.login2(use_name, 'Sta12345', '新注册用户')
        sleep(1)
        # 断言
        ass = AppAssertPage(self.driver)
        el = '参与共建热门部落'
        assert ass.is_element_present(MobileBy.ACCESSIBILITY_ID, el) == True,f'未找到元素{el}，断言失败'

    '''一键注册'''

    def test_single(self,start_app):
        self.driver = start_app
        step = LoginStep(self.driver)
        step.single()
        sleep(1)
        ass = AppAssertPage(self.driver)
        el = '参与共建热门部落'
        assert ass.is_element_present(MobileBy.ACCESSIBILITY_ID, el) == True,f'未找到元素{el}，断言失败'

    '''退出登录'''

    def test_logout(self,start_app):
        self.driver = start_app
        step = LoginStep(self.driver)
        step.logout()
        sleep(1)
        ass = AppAssertPage(self.driver)
        el = '账号'
        assert ass.is_element_present(MobileBy.ACCESSIBILITY_ID, el) == True,f'未找到元素{el}，断言失败'

    def test_switch_account_203(self,start_app):
        self.driver = start_app
        step = LoginStep(self.driver)
        step.switch_account_203()
        sleep(1)
        ass = AppAssertPage(self.driver)
        # 底部“部落”tab
        el = 'tribe_unselected_icon_light'
        assert ass.is_element_present(MobileBy.ACCESSIBILITY_ID, el) == True, f'未找到元素{el}，测试失败'

    def test_switch_account_202(self,start_app):
        self.driver = start_app
        step = LoginStep(self.driver)
        step.switch_account_202()
        sleep(1)
        ass = AppAssertPage(self.driver)
        # 底部“部落”tab
        el = 'tribe_unselected_icon_light'
        assert ass.is_element_present(MobileBy.ACCESSIBILITY_ID, el) == True, f'未找到元素{el}，测试失败'