from Base.base_page import BasePage
from PageObjct.element_page.IM_page import IMPage
from PageObjct.element_page.club_page import ClubPage


class IMStep(IMPage,ClubPage):
    '''IM相关操作'''

    '''频道发消息'''

    def IM_channel_message(self, text):
        # 选择侧边栏第一个部落
        self.click(self.el_club1)
        # 网卡的时候加载慢，使用显式等待
        self.driver.implicitly_wait(10)
        # 选择”聊天房间“房间
        self.click(self.el_choose_ChartRoom1)
        # 输入框内输入消息
        self.input(self.el_input_IM, text)
        # 发送消息
        self.click(self.el_send_message)

    '''频道发图片'''

    def IM_channel_picture(self):
        # 选择侧边栏第一个部落
        self.click(self.el_club1)
        # 选择”聊天房间“房间
        self.click(self.el_choose_ChartRoom1)
        # 点开更多面板
        self.click(self.el_IM_more)
        # 进入相册
        self.click(self.el_photo_choose)
        # 上滑两次确保到了相册顶部
        self.down_slide()
        self.down_slide()
        self.driver.implicitly_wait(10)
        # 选择第4张图片
        self.click(self.el_picture_choose)
        # 点击发送
        self.click(self.el_send_picture)

    '''频道发视频'''

    def IM_channel_video(self):
        # 选择侧边栏第一个部落
        self.click(self.el_club1)
        # 选择”聊天房间“房间
        self.click(self.el_choose_ChartRoom1)
        # 点开更多面板
        self.click(self.el_IM_more)
        # 进入相册
        self.click(self.el_photo_choose)
        # 上滑两次确保到了相册顶部
        self.down_slide()
        self.down_slide()
        self.driver.implicitly_wait(10)
        # 选择第2个视频
        self.click(self.el_video_choice)
        # 点击发送
        self.click(self.el_send_picture)

    '''单聊发消息'''
    def IM_solo_message(self,message):
        # 去消息tab
        self.click(self.el_message_icon)
        # 点击通讯录
        self.click(self.el_address_book)
        # 选择第六个好友
        self.click(self.el_choose_friend_six)
        # 输入框输入消息
        self.input(self.el_input_IM,message)
        # 点击发送
        self.click(self.el_send_message)

    '''单聊发图片'''

    def IM_solo_picture(self):
        # 去消息tab
        self.click(self.el_message_icon)
        # 点击通讯录
        self.click(self.el_address_book)
        # 选择第六个好友
        self.click(self.el_choose_friend_six)
        # 点开更多面板
        self.click(self.el_IM_more)
        # 进入相册
        self.click(self.el_photo_choose)
        # 上滑两次确保到了相册顶部
        self.down_slide()
        self.down_slide()
        self.driver.implicitly_wait(10)
        # 选择第4张图片
        self.click(self.el_picture_choose)
        # 点击发送
        self.click(self.el_send_picture)

    '''单聊发视频'''

    def IM_solo_video(self):
        # 去消息tab
        self.click(self.el_message_icon)
        # 点击通讯录
        self.click(self.el_address_book)
        # 选择第六个好友
        self.click(self.el_choose_friend_six)
        # 点开更多面板
        self.click(self.el_IM_more)
        # 进入相册
        self.click(self.el_photo_choose)
        # 上滑两次确保到了相册顶部
        self.down_slide()
        self.down_slide()
        self.driver.implicitly_wait(10)
        # 选择第2个视频
        self.click(self.el_video_choice)
        # 点击发送
        self.click(self.el_send_picture)

    '''群聊发消息'''

    def IM_group_message(self, message):
        # 去消息tab
        self.click(self.el_message_icon)
        # 点击通讯录
        self.click(self.el_address_book)
        # 点击我的群聊
        self.click(self.el_group_chart_list)
        # 选择第1个群聊
        self.click(self.el_choose_group_first)
        # 输入框输入消息
        self.input(self.el_input_IM, message)
        # 点击发送
        self.click(self.el_send_message)

    '''群聊发图片'''

    def IM_group_picture(self):
        # 去消息tab
        self.click(self.el_message_icon)
        # 点击通讯录
        self.click(self.el_address_book)
        # 点击我的群聊
        self.click(self.el_group_chart_list)
        # 选择第1个群聊
        self.click(self.el_choose_group_first)
        # 点开更多面板
        self.click(self.el_IM_more)
        # 进入相册
        self.click(self.el_photo_choose)
        # 上滑两次确保到了相册顶部
        self.down_slide()
        self.down_slide()
        self.driver.implicitly_wait(10)
        # 选择第4张图片
        self.click(self.el_picture_choose)
        # 点击发送
        self.click(self.el_send_picture)

    '''群聊发视频'''

    def IM_group_video(self):
        # 去消息tab
        self.click(self.el_message_icon)
        # 点击通讯录
        self.click(self.el_address_book)
        # 点击我的群聊
        self.click(self.el_group_chart_list)
        # 选择第1个群聊
        self.click(self.el_choose_group_first)
        # 点开更多面板
        self.click(self.el_IM_more)
        # 进入相册
        self.click(self.el_photo_choose)
        # 上滑两次确保到了相册顶部
        self.down_slide()
        self.down_slide()
        self.driver.implicitly_wait(10)
        # 选择第2个视频
        self.click(self.el_video_choice)
        # 点击发送
        self.click(self.el_send_picture)

    '''拉人建群'''
    def creat_group1(self):
        # 去消息tab
        self.click(self.el_message_icon)
        # 点击通讯录
        self.click(self.el_address_book)
        # 选择第六个好友
        self.click(self.el_choose_friend_six)
        # 进入聊天设置
        self.click(self.el_chart_setting)
        # 点击拉人创群
        self.click(self.el_chart_setting_add)
        # 拉人界面选择第一个好友
        self.click(self.el_add_first)
        # 点击确定
        self.click(self.el_add_done1)

    '''选人创建群聊'''
    def creat_group2(self):
        # 点击消息tab
        self.click(self.el_message_icon)
        # 点击+号
        self.click(self.el_add)
        # 点击发起群聊
        self.click(self.el_create_group)
        # 选择第一个好友
        self.click(self.el_add_first)
        # 选择第二个好友
        self.click(self.el_add_second)
        # 点击完成
        self.click(self.el_add_done2)
