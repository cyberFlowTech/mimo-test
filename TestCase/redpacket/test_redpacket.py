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


class TestRedPacket():
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

    '''单聊发红包'''

    def test_redpacket(self):
        self.setup()
        step = RedPacketStep(self.driver)
        step.create_redpacket1("0.01", "单聊自动化脚本红包", "111111")
        ass = AppAssertPage(self.driver)
        el = '单聊自动化脚本红包'
        sleep(1)
        assert ass.is_element_present(MobileBy.ACCESSIBILITY_ID, el) == True, '没有找到红包元素，测试失败'
        self.teardown()

    '''密码错误，发红包失败'''

    def test_redpacket_fail(self):
        self.setup()
        step = RedPacketStep(self.driver)
        step.create_redpacket1("0.01", "<UNK>", "111122")
        ass = AppAssertPage(self.driver)
        el = '验证失败'
        sleep(1)
        assert ass.is_element_present(MobileBy.ACCESSIBILITY_ID, el) == True, '缺少错误提示'
        self.teardown()

    '''单聊切币发红包'''

    def test_redpacket2(self):
        self.setup()
        step = RedPacketStep(self.driver)
        step.create_redpacket2("0.01", "CIQI自动化红包", "111111")
        ass = AppAssertPage(self.driver)
        el = 'CIQI自动化红包'
        sleep(1)
        assert ass.is_element_present(MobileBy.ACCESSIBILITY_ID, el) == True, '<UNK>'
        self.teardown()

    '''群聊发红包'''

    def test_group_redpacket(self):
        self.setup()
        step = RedPacketStep(self.driver)
        step.create_group_redpacket1('3', '0.04', '群聊自动化红包', '111111')
        ass = AppAssertPage(self.driver)
        el = '群聊自动化红包'
        sleep(1)
        assert ass.is_element_present(MobileBy.ACCESSIBILITY_ID, el) == True, '测试失败，未找到元素'
        self.teardown()

    '''群聊发ALG普通红包'''

    def test_group_redpacket2(self):
        self.setup()
        step = RedPacketStep(self.driver)
        step.create_group_redpacket2('3', '0.03', '群聊ALG自动化红包', '111111')
        ass = AppAssertPage(self.driver)
        el = '群聊ALG自动化红包'
        sleep(1)
        assert ass.is_element_present(MobileBy.ACCESSIBILITY_ID, el) == True, '<UNK>'
        self.teardown()

    '''频道发红包'''

    def test_channel_redpacket(self):
        self.setup()
        step = RedPacketStep(self.driver)
        step.create_channel_redpacket1('3', '0.04', '频道自动化红包', '111111')
        ass = AppAssertPage(self.driver)
        el = '频道自动化红包'
        sleep(1)
        assert ass.is_element_present(MobileBy.ACCESSIBILITY_ID, el) == True, '<UNK>'
        self.teardown()

    '''频道发CIQI普通红包'''

    def test_channel_redpacket2(self, start_app):
        # self.setup()
        self.driver = start_app
        step = RedPacketStep(self.driver)
        step.create_channel_redpacket2('3', '0.03', '频道CIQI自动化红包', '111111')
        ass = AppAssertPage(self.driver)
        el = '频道CIQI自动化红包'
        sleep(1)
        check.is_true(ass.is_element_enabled(MobileBy.ACCESSIBILITY_ID, el) == True), f'元素{el}应该可见但未找到'
        # self.teardown()
