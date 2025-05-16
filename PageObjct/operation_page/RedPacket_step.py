from appium.webdriver.common.mobileby import MobileBy
from selenium.common import ElementNotInteractableException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Base.app_assert_page import AppAssertPage
from PageObjct.element_page.IM_page import IMPage
from PageObjct.element_page.club_page import ClubPage


class RedPacketStep(ClubPage, IMPage):
    """红包相关操作封装"""

    '''寻找‘新赛季’部落'''
    def find_club(self):

        elements = self.driver.find_elements(
            By.XPATH,
            '//XCUIElementTypeApplication[@name="Zapry"]/XCUIElementTypeWindow[1]//XCUIElementTypeCollectionView/XCUIElementTypeCell/XCUIElementTypeOther/XCUIElementTypeImage'
        )

        for index, element in enumerate(elements, 1):
            print(f"正在点击第 {index} 个部落...")
            element.click()

            try:
                # 检查右侧窗口是否有"新赛季"文本
                season_text = self.driver.find_element(
                    By.XPATH,
                    '//XCUIElementTypeStaticText[@name="新赛季"]'
                )
                print(f"成功在第 {index} 个部落找到新赛季！")
                return True  # 找到后直接返回
            except NoSuchElementException:
                print(f"第 {index} 个部落不是新赛季部落")
                continue  # 继续下一个

        print("遍历完所有部落，未找到新赛季部落")
        return False



    '''单聊创建红包'''

    def create_redpacket1(self, sum, remark, pwd):

        # 去消息tab
        self.click(self.el_message_icon)
        # 切换到通讯录
        self.click(self.el_address_book)
        # 选择第6个好友
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH,
                                                         '//XCUIElementTypeApplication[@name="Zapry"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[7]')))
        self.click(self.el_choose_friend_six)
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
        self.input(self.el_solo_sum, sum)
        # 输入备注
        self.input(self.el_solo_remark, remark)
        # 创建红包
        self.click(self.el_create_redpacket)
        # 输入密码：
        self.input(self.el_input_pwd, pwd)

    '''切换CIQI币发红包'''

    def create_redpacket2(self, sum, remark, pwd):

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
        self.input(self.el_solo_sum, sum)
        # 输入备注
        self.input(self.el_solo_remark, remark)
        # 点击创建红包
        self.click(self.el_create_redpacket)
        # 输入密码
        self.input(self.el_input_pwd, pwd)

    '''群聊发红包'''

    def create_group_redpacket1(self, number, sum, remark, pwd):

        self.click(self.el_message_icon)
        self.click(self.el_address_book)
        self.click(self.el_group_chart_list)
        self.click(self.el_choose_group_first)
        self.click(self.el_IM_more)
        self.click(self.el_red_packet)
        self.input(self.el_group_number, number)
        self.input(self.el_solo_sum, sum)
        self.input(self.el_solo_remark, remark)
        self.click(self.el_create_redpacket)
        self.input(self.el_input_pwd, pwd)

    '''群聊发ALG普通红包'''

    def create_group_redpacket2(self, number, sum, remark, pwd):

        self.click(self.el_message_icon)
        self.click(self.el_address_book)
        self.click(self.el_message_icon)
        self.click(self.el_address_book)
        self.click(self.el_group_chart_list)
        self.click(self.el_choose_group_first)
        self.click(self.el_IM_more)
        self.click(self.el_red_packet)
        self.click(self.el_choose_redpacket_type)
        self.click(self.el_common_redpacket)
        self.input(self.el_group_number, number)
        self.click(self.el_choose_coin)
        self.click(self.el_choose_ALG)
        self.input(self.el_solo_sum, sum)
        self.input(self.el_solo_remark, remark)
        self.click(self.el_create_redpacket)
        self.input(self.el_input_pwd, pwd)

    '''频道发红包'''

    def create_channel_redpacket1(self, number, sum, remark, pwd):

        self.click(self.el_club1)
        self.click(self.el_choose_chart_room)
        self.click(self.el_IM_more)
        self.click(self.el_red_packet)
        self.input(self.el_channel_number, number)
        self.input(self.el_solo_sum, sum)
        self.input(self.el_solo_remark, remark)
        self.click(self.el_create_redpacket)
        self.input(self.el_input_pwd, pwd)

    '''频道发CIQI普通红包'''

    def create_channel_redpacket2(self, number, sum, remark, pwd):
        self.find_club()
        self.click(self.el_choose_chart_room)
        self.click(self.el_IM_more)
        self.click(self.el_red_packet)
        self.click(self.el_choose_redpacket_type)
        self.click(self.el_common_redpacket)
        self.input(self.el_channel_number, number)
        self.click(self.el_choose_coin)
        self.click(self.el_choose_CIQI)
        self.input(self.el_channel_sum, sum)
        self.input(self.el_channel_remark, remark)
        self.click(self.el_create_redpacket)
        self.input(self.el_input_pwd, pwd)

    '''领红包'''
    def receive_redpacket(self):
        self.click(self.el_red_packet)

