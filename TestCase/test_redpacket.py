from time import sleep
import pytest_check as check
from appium.webdriver.common.mobileby import MobileBy
from Base.app_assert_page import AppAssertPage
from PageObjct.element_page.IM_page import IMPage
from PageObjct.operation_page.IM_step import IMStep
from PageObjct.operation_page.RedPacket_step import RedPacketStep
from PageObjct.operation_page.login_step import LoginStep
from TestCase.test_login import TestLogin
from common.start_app import start_app


class TestRedPacket:
    '''发红包用例'''

    '''查看账号是否是202'''
    def test_account_is_202(self,start_app):
        self.driver = start_app.driver
        step = LoginStep(self.driver)
        step.account_is_202()
        ass = AppAssertPage(self.driver)
        el_ass = 'tribe_add_light'
        assert ass.is_element_present(MobileBy.ACCESSIBILITY_ID,el_ass) == True,\
            f'未找到元素{el_ass},不确定该账号是否为202'

    '''单聊发ALG红包'''

    def test_solo_alg(self, start_app):
        self.driver = start_app
        step = RedPacketStep(self.driver)
        # switch = LoginStep(self.driver)
        ass = AppAssertPage(self.driver)
        # 发红包
        step.create_redpacket_alg("203", "0.01", "单聊自动化ALG红包", "111111")
        el_ass = '单聊自动化ALG红包'
        sleep(2)
        # 断言：红包发送成功
        assert ass.is_element_displayed(MobileBy.ACCESSIBILITY_ID, el_ass) == True, \
            f'未找到元素{el_ass},单聊发ALG红包失败'
        # # 切换到203账号
        # switch.switch_account_203()
        # # 领红包
        # step.open_solo_alg()
        # sleep(2)
        # el2 = '已被领完，1个红包共0.01 CIQI'
        # # 断言：领取红包成功
        # assert ass.is_element_displayed(MobileBy.ACCESSIBILITY_ID, el2) == True, f'未找到元素{el2},测试失败'

    '''密码错误，发红包提示'''

    def test_pwd_fail(self, start_app):
        self.driver = start_app
        step = RedPacketStep(self.driver)
        step.create_redpacket_alg("203", "0.01", "<UNK>", "111122", )
        ass = AppAssertPage(self.driver)
        el_ass = '验证失败'
        sleep(2)
        assert ass.is_element_present(MobileBy.ACCESSIBILITY_ID, el_ass) == True, \
            f'未找到错误提示消息{el_ass}，测试失败'

    '''单聊切币发CIQI红包'''

    def test_solo_ciqi(self, start_app):
        self.driver = start_app
        step = RedPacketStep(self.driver)
        step.receive_solo_ciqi("203", "0.01", "单聊自动化CIQI红包", "111111")
        ass = AppAssertPage(self.driver)
        el_ass = '单聊自动化CIQI红包'
        sleep(2)
        assert ass.is_element_present(MobileBy.ACCESSIBILITY_ID, el_ass) == True, \
            f'未找到元素{el_ass}，单聊发CIQI红包失败'

    '''群聊发CIQI拼手气红包'''

    def test_group_lucky_ciqi(self, start_app):
        self.driver = start_app
        step = RedPacketStep(self.driver)
        step.create_group_luck_ciqi('1111', '3', '0.04', '群聊自动化CIQI拼手气红包', '111111')
        ass = AppAssertPage(self.driver)
        el = '群聊自动化CIQI拼手气红包'
        sleep(2)
        assert ass.is_element_present(MobileBy.ACCESSIBILITY_ID, el) == True, \
            f'未找到元素{el},群聊发CIQI拼手气红包失败'

    '''群聊发ALG普通红包'''

    def test_group_common_alg(self, start_app):
        self.driver = start_app
        step = RedPacketStep(self.driver)
        step.create_group_common_alg('1111', '3', '0.03', '群聊自动化ALG普通红包', '111111')
        ass = AppAssertPage(self.driver)
        el = '群聊自动化ALG普通红包'
        sleep(2)
        assert ass.is_element_present(MobileBy.ACCESSIBILITY_ID, el) == True, \
            f'未找到元素{el},群聊发ALG普通红包失败'

    '''频道发ALG拼手气红包'''

    def test_channel_lucky_alg(self, start_app):
        self.driver = start_app
        step = RedPacketStep(self.driver)
        step.create_channel_luck_alg('3', '0.04', '频道自动化ALG拼手气红包', '111111')
        ass = AppAssertPage(self.driver)
        el = '频道自动化ALG拼手气红包'
        sleep(2)
        assert ass.is_element_present(MobileBy.ACCESSIBILITY_ID, el) == True, \
            f'未找到元素{el},频道发ALG拼手气红包失败'

    '''频道发CIQI普通红包'''

    def test_channel_common_ciqi(self, start_app):
        self.driver = start_app
        step = RedPacketStep(self.driver)
        step.create_channel_common_ciqi('3', '0.03', '频道自动化CIQI普通红包', '111111')
        ass = AppAssertPage(self.driver)
        el = '频道自动化CIQI普通红包'
        sleep(2)
        assert ass.is_element_enabled(MobileBy.ACCESSIBILITY_ID, el) == True, \
            f'未找到元素{el},频道发CIQI普通红包失败'

    '''切换账号'''

    def test_change_account_203(self, start_app):
        self.driver = start_app
        step = LoginStep(self.driver)
        step.switch_account_203()
        ass = AppAssertPage(self.driver)
        # 底部“部落”tab
        el = 'tribe_unselected_icon_light'
        assert ass.is_element_present(MobileBy.ACCESSIBILITY_ID, el) == True, \
            f'未找到元素{el}，切换账号失败'

    '''领取单聊ALG红包'''

    def test_open_solo_alg(self, start_app):
        self.driver = start_app
        step = RedPacketStep(self.driver)
        step.open_solo_alg()
        ass = AppAssertPage(self.driver)
        el_ass = '已被领完，1个红包共0.01 ALG'
        # 断言：领取红包成功
        assert ass.is_element_displayed(MobileBy.ACCESSIBILITY_ID, el_ass) == True, \
            f'未找到元素{el_ass},领取单聊ALG红包失败'

    '''领取单聊CIQI红包'''

    def test_open_solo_ciqi(self, start_app):
        self.driver = start_app
        step = RedPacketStep(self.driver)
        step.open_solo_ciqi()
        ass = AppAssertPage(self.driver)
        el_ass = '已被领完，1个红包共0.01 CIQI'
        # 断言：领取红包成功
        assert ass.is_element_displayed(MobileBy.ACCESSIBILITY_ID, el_ass) == True, \
            f'未找到元素{el_ass},领取单聊CIQI红包失败'

    '''领取群聊ALG普通红包'''

    def test_open_group_common_alg(self, start_app):
        self.driver = start_app
        step = RedPacketStep(self.driver)
        step.open_group_common_alg()
        ass = AppAssertPage(self.driver)
        el_ass1 = 'new202的红包'
        el_ass2 = '群聊自动化ALG普通红包'
        # 断言：领取红包成功
        assert ass.is_element_displayed(MobileBy.ACCESSIBILITY_ID, el_ass1) == True, \
            f'未找到元素{el_ass1},领取群聊ALG普通红包失败'
        assert ass.is_element_displayed(MobileBy.ACCESSIBILITY_ID, el_ass2) == True, \
            f'未找到元素{el_ass2},领取群聊ALG普通红包失败'

    '''领取群聊CIQI拼手气红包'''

    def test_open_group_lucky_ciqi(self, start_app):
        self.driver = start_app
        step = RedPacketStep(self.driver)
        step.open_group_lucky_ciqi()
        ass = AppAssertPage(self.driver)
        el_ass1 = 'new202的红包'
        el_ass2 = '群聊自动化CIQI拼手气红包'
        # 断言：领取红包成功
        assert ass.is_element_displayed(MobileBy.ACCESSIBILITY_ID, el_ass1) == True, \
            f'未找到元素{el_ass1},领取群聊CIQI拼手气红包失败'
        assert ass.is_element_displayed(MobileBy.ACCESSIBILITY_ID, el_ass2) == True, \
            f'未找到元素{el_ass2},领取群聊CIQI拼手气红包失败'

    '''领取频道ALG拼手气红包'''

    def test_open_channel_lucky_alg(self, start_app):
        self.driver = start_app
        step = RedPacketStep(self.driver)
        step.open_channel_lucky_alg()
        ass = AppAssertPage(self.driver)
        el_ass1 = 'new202的红包'
        el_ass2 = '频道自动化ALG拼手气红包'
        # 断言：领取红包成功
        assert ass.is_element_displayed(MobileBy.ACCESSIBILITY_ID, el_ass1) == True, \
            f'未找到元素{el_ass1},领取频道ALG拼手气红包失败'
        assert ass.is_element_displayed(MobileBy.ACCESSIBILITY_ID, el_ass2) == True, \
            f'未找到元素{el_ass2},领取频道ALG拼手气红包失败'

    '''领取频道CIQI普通红包'''

    def test_open_channel_common_ciqi(self, start_app):
        self.driver = start_app
        step = RedPacketStep(self.driver)
        step.open_channel_common_ciqi()
        ass = AppAssertPage(self.driver)
        el_ass1 = 'new202的红包'
        el_ass2 = '频道自动化CIQI普通红包'
        # 断言：领取红包成功
        assert ass.is_element_displayed(MobileBy.ACCESSIBILITY_ID, el_ass1) == True, \
            f'未找到元素{el_ass1},领取频道CIQI普通红包失败'
        assert ass.is_element_displayed(MobileBy.ACCESSIBILITY_ID, el_ass2) == True, \
            f'未找到元素{el_ass2},领取频道CIQI普通红包失败'
