
from time import sleep
import pytest_check as check
from appium.webdriver.common.mobileby import MobileBy
from Base.app_assert_page import AppAssertPage
from PageObjct.operation_page.RedPacket_step import RedPacketStep
from PageObjct.operation_page.login_step import LoginStep
from TestCase.test_login import TestLogin
from common.start_app import start_app


class TestRedPacket:

    '''发红包用例'''

    '''单聊发ALG红包'''

    def test_solo_alg(self, start_app):

        self.driver = start_app
        step = RedPacketStep(self.driver)
        switch = LoginStep(self.driver)
        ass = AppAssertPage(self.driver)

        # 发红包
        step.create_redpacket_alg("203", "0.01", "单聊自动化ALG红包", "111111")
        el = '单聊自动化ALG红包'
        sleep(1)
        # 断言：红包发送成功
        assert ass.is_element_displayed(MobileBy.ACCESSIBILITY_ID, el) == True, f'未找到元素{el},测试失败'
        # 切换到203账号
        switch.switch_account_203()
        # 领红包
        step.receive_solo_alg()
        sleep(2)
        el2 = '已被领完，1个红包共0.01 CIQI'
        # 断言：领取红包成功
        assert ass.is_element_displayed(MobileBy.ACCESSIBILITY_ID, el2) == True, f'未找到元素{el2},测试失败'


    '''密码错误，发红包提示'''

    def test_pwd_fail(self, start_app):
        self.driver = start_app
        step = RedPacketStep(self.driver)
        step.create_redpacket_alg("203","0.01", "<UNK>", "111122", )
        ass = AppAssertPage(self.driver)
        el = '验证失败'
        sleep(1)
        assert ass.is_element_present(MobileBy.ACCESSIBILITY_ID, el) == True, '未找到错误提示消息，测试失败'

    '''单聊切币发CIQI红包'''

    def test_solo_ciqi(self, start_app):
        self.driver = start_app
        step = RedPacketStep(self.driver)
        step.create_redpacket_ciqi("0.01", "单聊自动化CIQI红包", "111111")
        ass = AppAssertPage(self.driver)
        el = '单聊自动化CIQI红包'
        sleep(1)
        assert ass.is_element_present(MobileBy.ACCESSIBILITY_ID, el) == True, '<UNK>'

    '''群聊发CIQI拼手气红包'''

    def test_group_redpacket(self, start_app):
        self.driver = start_app
        step = RedPacketStep(self.driver)
        step.create_group_redpacket1('3', '0.04', '群聊自动化CIQI拼手气红包', '111111')
        ass = AppAssertPage(self.driver)
        el = '群聊自动化CIQI拼手气红包'
        sleep(1)
        assert ass.is_element_present(MobileBy.ACCESSIBILITY_ID, el) == True, f'未找到元素{el},测试失败'

    '''群聊发ALG普通红包'''

    def test_group_redpacket2(self, start_app):
        self.driver = start_app
        step = RedPacketStep(self.driver)
        step.create_group_redpacket2('3', '0.03', '群聊自动化ALG普通红包', '111111')
        ass = AppAssertPage(self.driver)
        el = '群聊自动化ALG普通红包'
        sleep(1)
        assert ass.is_element_present(MobileBy.ACCESSIBILITY_ID, el) == True, f'未找到元素{el},测试失败'

    '''频道发ALG拼手气红包'''

    def test_channel_redpacket(self, start_app):
        self.driver = start_app
        step = RedPacketStep(self.driver)
        step.create_channel_redpacket1('3', '0.04', '频道自动化ALG拼手气红包', '111111')
        ass = AppAssertPage(self.driver)
        el = '频道自动化ALG拼手气红包'
        sleep(1)
        assert ass.is_element_present(MobileBy.ACCESSIBILITY_ID, el) == True, f'未找到元素{el},测试失败'

    '''频道发CIQI普通红包'''

    def test_channel_redpacket2(self, start_app):
        self.driver = start_app
        step = RedPacketStep(self.driver)
        step.create_channel_redpacket2('3', '0.03', '频道自动化CIQI普通红包', '111111')
        ass = AppAssertPage(self.driver)
        el = '频道自动化CIQI普通红包'
        sleep(1)
        check.is_true(ass.is_element_enabled(MobileBy.ACCESSIBILITY_ID, el) == True,f'未找到元素{el},测试失败')

