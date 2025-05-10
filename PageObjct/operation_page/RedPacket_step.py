from selenium.common import ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from PageObjct.element_page.IM_page import IMPage
from PageObjct.element_page.club_page import ClubPage


class RedPacketStep(ClubPage, IMPage):

    def create_redpacket1(self, sum, remark, pwd):
        '''单聊创建红包'''
        # 去消息tab
        self.click(self.el_message_icon)
        # 切换到通讯录
        self.click(self.el_address_book)
        # 选择第6个好友
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH,
                                                         '//XCUIElementTypeApplication[@name="Zapry"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[7]')))
        # 聊天室点击+按钮
        self.click(self.el_IM_more)
        # 点击红包
        self.click(self.el_red_packet)
        # 检查有没有没绑钱包提示，没绑先绑
        element1 = self.driver.find_elements(By.XPATH, '//XCUIElementTypeButton[@name="立即设置"]')
        if element1:
            element1[0].click()
            self.click(self.el_recognition_skip)
            # 支付密码设置为6个1
            for i in range(12):
                self.click(self.el_PayPwd)
            try:
                element2 = WebDriverWait(self.driver, 10).until(
                    expected_conditions.element_to_be_clickable(
                        (By.XPATH, '//XCUIElementTypeNavigationBar[@name="RNSScreen"]/XCUIElementTypeOther[3]')))
                # 关闭钱包回到聊天室
                element2.click()
            except TimeoutError as e:
                print(f"{e}")
            except ElementNotInteractableException as e:
                print(f'{e}')
            # +号菜单
            self.click(self.el_IM_more)
            # 红包
            self.click(self.el_red_packet)

        else:
            pass
        # 输入金额
        self.input(self.el_sum, sum)
        # 输入备注
        self.input(self.el_red_remark, remark)
        # 创建红包
        self.click(self.el_create_redpacket)
        # 输入密码：
        self.input(self.el_input_pwd, pwd)

    def create_redpacket2(self, sum, remark, pwd):
        '''切换CIQI币发红包'''
        # 点击消息tab
        self.click(self.el_message_icon)
        # 点击通讯录
        self.click(self.el_address_book)
        # 加载好友列表，点击第六个好友进入聊天室
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH,
                                                                                          '//XCUIElementTypeApplication[@name="Zapry"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[7]')))
        # 聊天室中点击右下角的+号按钮
        self.click(self.el_IM_more)
        # 点击红包
        self.click(self.el_red_packet)
        # 点击下拉icon
        self.click(self.el_choose_coin)
        # 代币列表浮层中选择CIQI币
        self.click(self.el_choose_CIQI)
        # 输入金额
        self.input(self.el_sum, sum)
        # 输入备注
        self.input(self.el_red_remark, remark)
        # 点击创建红包
        self.click(self.el_create_redpacket)
        # 输入密码
        self.input(self.el_input_pwd, pwd)
