import os
from appium import webdriver
from selenium.webdriver.common.by import By
from Base.app_assert_page import AppAssertPage
from PageObjct.operation_page.RedPacket_step import RedPacketStep
from common.data_util import readYaml
from common.start_app import StartApp


class TestRedPacket(StartApp):
    def set_up(self):
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
        self.set_up()
        step = RedPacketStep(self.driver)
        step.create_redpacket1("0.01", "自动化脚本红包", "111111")
        ass = AppAssertPage(self.driver)
        el = '<UNK>'
        assert ass.is_element_present(By.XPATH, el) == True, '没有找到红包元素，测试失败'
        self.teardown()

        '''单聊切币发红包'''

    def test_choose_CIQI(self):
        self.set_up()
        step = RedPacketStep(self.driver)
        step.create_redpacket2("0.01", "CIQI自动化红包", "111111")
        ass = AppAssertPage(self.driver)
        el = '<UNK>'
        assert ass.is_element_present(By.XPATH, el) == True, '<UNK>'
        self.teardown()
