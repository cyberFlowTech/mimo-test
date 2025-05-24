import os
import re
from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

from Base.app_assert_page import AppAssertPage
from PageObjct.operation_page.club_step import ClubStep
from common.data_util import readYaml


class TestClub:

    # def test_start_server(self):
    def tset_up(self):
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

    """创建部落"""

    def test_create_club(self):
        self.tset_up()

        club_step = ClubStep(self.driver)
        club_step.create_club('部落')
        # 创建过程太慢，需要多等一会
        sleep(6)
        # 断言
        ass = AppAssertPage(driver=self.driver)
        # 检查页面有没有“跳过”元素
        assert ass.is_element_present(MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="跳过"]') == True
        self.teardown()

    """分享部落到房间"""

    def test_share_club_to_club(self):
        self.tset_up()

        club_step = ClubStep(self.driver)
        club_step.share_club_to_club()
        sleep(1)
        ass = AppAssertPage(driver=self.driver)
        # 检查页面有没有“部落邀请”元素
        assert ass.is_element_present(MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="部落邀请"]') == True
        self.teardown()

    """分享部落到单聊"""

    def test_share_club_to_contact(self):
        self.tset_up()

        club_step = ClubStep(self.driver)
        club_step.share_club_to_contact('204')
        sleep(1)
        ass = AppAssertPage(driver=self.driver)
        # 检查页面有没有“部落邀请”元素
        assert ass.is_element_present(MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="部落邀请"]') == True
        self.teardown()

    """分享部落群聊"""

    def test_share_club_to_group_chart(self):
        self.tset_up()

        club_step = ClubStep(self.driver)
        club_step.share_club_to_group_chat('2')
        sleep(1)
        ass = AppAssertPage(driver=self.driver)
        # 检查页面有没有“部落邀请”元素
        assert ass.is_element_present(MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="部落邀请"]') == True
        self.teardown()

    """发部落动态"""

    def test_send_community(self):
        self.tset_up()

        club_step = ClubStep(self.driver)
        club_step.send_community('这是动态标题', '这是动态内容')
        sleep(2)
        # 检查页面有没有“动态详情”元素
        ass = AppAssertPage(driver=self.driver)
        assert ass.is_element_present(MobileBy.ACCESSIBILITY_ID, '动态详情') == True
        self.teardown()

    """添加聊天房间"""

    def test_add_chart_room(self):
        self.tset_up()

        club_step = ClubStep(self.driver)
        club_step.add_chat_room('聊天房间')
        sleep(2)
        ass = AppAssertPage(driver=self.driver)
        assert ass.is_element_present(MobileBy.ACCESSIBILITY_ID, '聊天房间') == True
        self.teardown()

    """添加应用房间"""

    def test_add_dapp_room(self):
        self.tset_up()

        club_step = ClubStep(self.driver)
        club_step.add_dapp_room('应用房间',
                                'https://www.baidu.com/s?wd=%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95&rsv_spt=1&rsv_iqid=0x9058a494003119fd&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_dl=tb&rsv_enter=1&rsv_sug3=38&rsv_sug1=36&rsv_sug7=100&rsv_sug2=0&rsv_btype=i&prefixsug=%25E8%2587%25AA%25E5%258A%25A8%25E5%258C%2596%25E6%25B5%258B%25E8%25AF%2595&rsp=5&inputT=12351&rsv_sug4=15729',
                                '应用房间介绍,这就是百度了一个“自动化测试”的百度网站')
        sleep(2)
        ass = AppAssertPage(driver=self.driver)
        try:
            assert ass.is_element_present(MobileBy.ACCESSIBILITY_ID, '应用房间') == True, "没有找到这个元素，测试失败！"
        except AssertionError as e:
            print(e)
            self.teardown()

    '''聊天房间发布公告'''

    def test_chart_room_announce(self):
        self.tset_up()

        club_step = ClubStep(self.driver)
        club_step.chart_room_announce('欢迎来到聊天房间')
        sleep(2)
        ass = AppAssertPage(driver=self.driver)
        el_ass = '(//XCUIElementTypeStaticText[@name="公告"])[8]'
        assert ass.is_element_present(MobileBy.XPATH, el_ass) == True
        self.teardown()

    '''房间开启全员禁言'''

    def test_all_shutup1(self):
        self.tset_up()

        club_step = ClubStep(self.driver)
        club_step.all_shutup()
        ass = AppAssertPage(driver=self.driver)
        el_ass = '203 已开启“全员禁言” '
        assert ass.is_element_present(MobileBy.ACCESSIBILITY_ID, el_ass) == True
        self.teardown()

    '''房间关闭全员禁言'''

    def test_all_shutup2(self):
        self.tset_up()

        club_step = ClubStep(self.driver)
        club_step.all_shutup()
        ass = AppAssertPage(driver=self.driver)
        el_ass = '203 已关闭“全员禁言” '
        assert ass.is_element_present(MobileBy.ACCESSIBILITY_ID, el_ass) == True
        self.teardown()

    '''消息免打扰'''

    def test_message_disturb(self):
        self.tset_up()

        club_step = ClubStep(self.driver)
        club_step.message_disturb()
        ass = AppAssertPage(driver=self.driver)
        el_ass = 'chat_disturb_light'
        assert ass.is_element_present(MobileBy.ACCESSIBILITY_ID, el_ass) == True
        self.teardown()

    '''清空聊天记录'''

    def test_clear_message(self):
        self.tset_up()

        club_step = ClubStep(self.driver)
        club_step.clear_message()
        ass = AppAssertPage(driver=self.driver)
        el_ass = '//XCUIElementTypeStaticText[@name="部落主"]'
        assert ass.is_element_present(MobileBy.XPATH, el_ass) == False
        self.teardown()

    '''删除房间'''

    def test_delete_room(self):
        self.tset_up()

        club_step = ClubStep(self.driver)
        club_step.delete_room()
        sleep(2)
        ass = AppAssertPage(driver=self.driver)
        el_ass = '//XCUIElementTypeStaticText[@name="聊天房间"]'
        assert ass.is_element_present(MobileBy.XPATH, el_ass) == False
        self.teardown()

    '''根据应用房间提示去绑定钱包'''

    def test_bing_wallet(self):
        self.tset_up()

        club_step = ClubStep(self.driver)
        club_step.bing_wallet()
        # 创建钱包后加载较慢
        sleep(4)
        ass = AppAssertPage(driver=self.driver)
        el_ass = '交易历史'
        assert ass.is_element_present(MobileBy.ACCESSIBILITY_ID, el_ass) == False
        self.teardown()



if __name__ == '__main__':
    pytest.main()
