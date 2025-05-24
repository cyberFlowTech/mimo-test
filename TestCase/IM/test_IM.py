from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from Base.app_assert_page import AppAssertPage
from PageObjct.operation_page.IM_step import IMStep
from common.start_app import start_app


class TestIM:
    """频道发消息"""
    def test_IM_channel_message(self,start_app):
        self.driver = start_app

        club_step = IMStep(self.driver)
        club_step.IM_channel_message('频道自动化消息')

        ass = AppAssertPage(driver=self.driver)
        el = "频道自动化消息"
        assert ass.is_element_present(MobileBy.ACCESSIBILITY_ID,el) == True

    '''在频道发图片'''
    def test_IM_channel_picture(self,start_app):
        self.driver = start_app

        club_step = IMStep(self.driver)
        club_step.IM_channel_picture()
        # 多等一会让图片发送成功
        sleep(2)
        ass = AppAssertPage(driver=self.driver)
        # 被检查的元素
        el_ass = '/var/mobile/Containers/Data/Application/0DB0277E-94E9-4047-98E2-4932E00004F5/Library/Caches/1744789632269_4A1D0F12-BD50-4546-BA6F-81505E52941E.jpg'
        assert ass.is_element_present(MobileBy.ACCESSIBILITY_ID, el_ass) == True

    '''在频道发视频'''
    def test_IM_channel_video(self,start_app):
        self.driver = start_app

        club_step = IMStep(self.driver)
        club_step.IM_channel_video()
        sleep(2)
        ass = AppAssertPage(driver=self.driver)
        # 被检查的元素
        el_ass = '/var/mobile/Containers/Data/Application/0DB0277E-94E9-4047-98E2-4932E00004F5/Library/Caches/1744789632269_4A1D0F12-BD50-4546-BA6F-81505E52941E.jpg'
        assert ass.is_element_present(MobileBy.ACCESSIBILITY_ID, el_ass) == True

    '''单聊发消息'''
    def test_IM_solo_message(self,start_app):
        self.driver = start_app
        step = IMStep(self.driver)
        step.IM_solo_message("自动化单聊消息")
