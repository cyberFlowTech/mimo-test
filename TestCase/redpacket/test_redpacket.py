import os
from time import sleep
import pytest_check as check
import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from Base.app_assert_page import AppAssertPage
from PageObjct.operation_page.RedPacket_step import RedPacketStep
from common.data_util import readYaml
from common.start_app import start_app


class TestRedPacket:
    '''发红包用例'''

    '''单聊发红包'''

    def test_redpacket(self, start_app):
        self.driver = start_app
        step = RedPacketStep(self.driver)
        step.create_redpacket1("0.01", "单聊自动化脚本红包", "111111")
        ass = AppAssertPage(self.driver)
        el = '单聊自动化脚本红包'
        sleep(1)
        assert ass.is_element_present(MobileBy.ACCESSIBILITY_ID, el) == True, '没有找到红包元素，测试失败'

    '''密码错误，发红包提示'''

    def test_redpacket_fail(self, start_app):
        self.driver = start_app
        step = RedPacketStep(self.driver)
        step.create_redpacket1("0.01", "<UNK>", "111122")
        ass = AppAssertPage(self.driver)
        el = '验证失败'
        sleep(1)
        assert ass.is_element_present(MobileBy.ACCESSIBILITY_ID, el) == True, '缺少错误提示'

    '''单聊切币发红包'''

    def test_redpacket2(self, start_app):
        self.driver = start_app
        step = RedPacketStep(self.driver)
        step.create_redpacket2("0.01", "CIQI自动化红包", "111111")
        ass = AppAssertPage(self.driver)
        el = 'CIQI自动化红包'
        sleep(1)
        assert ass.is_element_present(MobileBy.ACCESSIBILITY_ID, el) == True, '<UNK>'

    '''群聊发红包'''

    def test_group_redpacket(self, start_app):
        self.driver = start_app
        step = RedPacketStep(self.driver)
        step.create_group_redpacket1('3', '0.04', '群聊自动化红包', '111111')
        ass = AppAssertPage(self.driver)
        el = '群聊自动化红包'
        sleep(1)
        assert ass.is_element_present(MobileBy.ACCESSIBILITY_ID, el) == True, '测试失败，未找到元素'

    '''群聊发ALG普通红包'''

    def test_group_redpacket2(self, start_app):
        self.driver = start_app
        step = RedPacketStep(self.driver)
        step.create_group_redpacket2('3', '0.03', '群聊ALG自动化红包', '111111')
        ass = AppAssertPage(self.driver)
        el = '群聊ALG自动化红包'
        sleep(1)
        assert ass.is_element_present(MobileBy.ACCESSIBILITY_ID, el) == True, '<UNK>'

    '''频道发红包'''

    def test_channel_redpacket(self, start_app):
        self.driver = start_app
        step = RedPacketStep(self.driver)
        step.create_channel_redpacket1('3', '0.04', '频道自动化红包', '111111')
        ass = AppAssertPage(self.driver)
        el = '频道自动化红包'
        sleep(1)
        assert ass.is_element_present(MobileBy.ACCESSIBILITY_ID, el) == True, '<UNK>'

    '''频道发CIQI普通红包'''

    def test_channel_redpacket2(self, start_app):
        self.driver = start_app
        step = RedPacketStep(self.driver)
        step.create_channel_redpacket2('3', '0.03', '频道CIQI自动化红包', '111111')
        ass = AppAssertPage(self.driver)
        el = '频道CIQI自动化红包'
        sleep(1)
        check.is_true(ass.is_element_enabled(MobileBy.ACCESSIBILITY_ID, el) == True), f'元素{el}应该可见但未找到'
