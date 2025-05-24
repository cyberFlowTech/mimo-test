
from time import sleep

from PageObjct.element_page.IM_page import IMPage
from PageObjct.element_page.club_page import ClubPage



class ClubStep(ClubPage, IMPage):
    """创建部落"""

    def create_club(self, name):

        # 点击icon
        self.click(self.el_icon)
        # 点击卡片
        self.click(self.el_create)
        # 部落头像
        self.click(self.el_photo)
        # 选择照片
        self.click(self.el_choose)
        # 点击完成
        self.click(self.el_finish)
        # 太快了找不到元素
        sleep(1)
        # 裁剪完成
        self.click(self.el_tailor)
        # 输入部落名
        self.input(self.el_name, name)
        # 点击创建部落
        self.click(self.el_create_club)

    '''分享部落到频道'''

    def share_club_to_club(self):
        # 点击侧边栏第一个部落
        self.click(self.el_club1)
        # 点击分享
        self.click(self.el_share)
        # 点击邀请好友
        self.click(self.el_invite_IM)
        # 选择部落
        self.click(self.el_my_club)
        # 选择第二个部落
        self.click(self.el_second_club)
        sleep(1)
        # 选择聊天房间
        self.click(self.el_choose_chart_room)
        sleep(1)
        # 点击完成
        self.click(self.el_share_club_done)
        sleep(1)
        # 分享弹窗点击发送
        self.click(self.el_share_send)

    """分享部落到单聊"""

    def share_club_to_contact(self, contact_name):
        # 点击侧边栏第一个部落
        self.click(self.el_club1)
        # 点击分享
        self.click(self.el_share)
        # 点击邀请好友
        self.click(self.el_invite_IM)
        # 点击我的联系人item
        self.click(self.el_my_contacts)
        # 我的联系人内部搜索输入框中输入
        self.input(self.el_contacts_search, contact_name)
        sleep(1)
        # 点击搜索结果中的第一个联系人的名字
        self.click(self.el_first_name)
        sleep(1)
        # 点击确认
        self.click(self.el_confirm)
        sleep(1)
        # 外部聚合页点击完成
        self.click(self.el_share_done)
        # 分享弹窗点击发送
        self.click(self.el_share_send)

    '''分享部落到群聊'''

    def share_club_to_group_chat(self, group_name):
        # 点击侧边栏第一个部落
        self.click(self.el_club1)
        # 点击分享
        self.click(self.el_share)
        # 点击邀请好友
        self.click(self.el_invite_IM)
        sleep(1)
        # 选择群聊
        self.click(self.el_my_group)
        # 搜索群名
        self.input(self.el_group_search, group_name)
        sleep(1)
        # 选择第一个群聊
        self.click(self.el_share_group_first)
        sleep(1)
        # 点击确认
        self.click(self.el_group_confirm)
        sleep(1)
        # 分享弹窗点击发送
        self.click(self.el_share_send)

    '''发一条部落动态'''

    def send_community(self, title, text):
        # 点击进入部落社区
        self.click(self.el_community)
        # 点击写动态按钮
        self.click(self.el_send_community)
        # 输入标题
        self.input(self.el_head_title, title)
        # 输入正文
        self.input(self.el_body_text, text)
        # 点击发布
        self.click(self.el_release)

    '''添加聊天房间'''

    def add_chat_room(self, chart_room):
        # 点击 部落管理 后面的 + 号
        self.click(self.el_add_room)
        # 选择聊天房间
        self.click(self.el_chart_room)
        # 输入房间名
        self.input(self.el_chart_name, chart_room)
        # 创建房间
        self.click(self.el_create_button)

    '''添加DAPP房间'''

    def add_dapp_room(self, dapp_room, dapp_link, dapp_text):
        # 点击 部落管理 后面的 + 号
        self.click(self.el_add_room)
        # 选择应用房间
        self.click(self.el_dapp_room)
        # 输入应用房间名
        self.input(self.el_dapp_name, dapp_room)
        # 输入链接
        self.input(self.el_dapp_link, dapp_link)
        # 输入介绍
        self.input(self.el_dapp_text, dapp_text)
        # 创建应用房间
        self.click(self.el_dapp_done)
        # self.swipe(123,123,432,422)

    '''发布房间公告'''

    def chart_room_announce(self, text):
        # 选择侧边栏第一个部落
        self.click(self.el_club1)
        # 选择“聊天房间”房间
        self.click(self.el_choose_ChartRoom1)
        # 进入房间信息
        self.click(self.el_chart_room_information)
        # 打开房间公告
        self.click(self.el_announce)
        # 输入内容
        self.input(self.el_announce_content, text)
        # 发布公告
        self.click(self.el_announcement)
        # 返回房间
        self.click(self.el_back)

    '''开启全员禁言'''

    def all_shutup(self):
        # 选择侧边栏第一个部落
        self.click(self.el_club1)
        # 选择“日常聊天”房间
        self.click(self.el_choose_ChartRoom1)
        # 进入房间信息
        self.click(self.el_chart_room_information)
        # 开启全员禁言
        self.click(self.el_all_Shutup)
        # 返回房间
        self.click(self.el_back)

    '''设置免打扰'''

    def message_disturb(self):
        # 选择侧边栏第一个部落
        self.click(self.el_club1)
        # 选择“聊天房间”房间
        self.click(self.el_choose_ChartRoom1)
        # 进入房间信息
        self.click(self.el_choose_ChartRoom1)
        # 点击免打扰唤起浮层
        self.click(self.el_all_Shutup)
        # 选择“不允许通知”
        self.click(self.el_no_disturb)
        # 返回房间
        self.click(self.el_back)

    '''清空聊天记录'''

    def clear_message(self):
        # 选择侧边栏第一个部落
        self.click(self.el_club1)
        # 选择“聊天房间”房间
        self.click(self.el_choose_ChartRoom1)
        # 进入房间信息
        self.click(self.el_chart_room_information)
        # 点击清空聊天记录
        self.click(self.el_clear_message)
        # 二次确认
        self.click(self.el_clear_popup)
        # 返回
        self.click(self.el_back)

    '''删除房间'''

    def delete_room(self):
        # 选择侧边栏第一个部落
        self.click(self.el_club1)
        # 选择“聊天房间”房间
        self.click(self.el_choose_ChartRoom1)
        # 进入房间信息
        self.click(self.el_chart_room_information)
        # 删除房间
        self.click(self.el_delete_room)
        # 二次确认
        self.click(self.el_delete_popup)

    '''通过应用房间提示绑定钱包'''

    def bing_wallet(self):
        # 选择第一个部落
        self.click(self.el_club1)
        # 点击应用房间
        self.click(self.el_choose_DappRoom)
        # 跳转到绑定钱包页面
        self.click(self.el_popup_BindWallet)
        # 创建新钱包
        self.click(self.el_create_NewWallet)
        # 二次确认
        self.click(self.el_popup_NewWallet)
        # 跳过生物识别
        self.click(self.el_recognition_skip)
        # 输入密码并二次确认密码
        for i in range(12):
            self.click(self.el_PayPwd)

    '''最小化dapp'''

    def dapp_windowed(self):
        # 进入第一个部落
        self.click(self.el_club1)
        # 选择dapp房间
        self.click(self.el_choose_DappRoom)
        # 弹窗点击确定
        try:
            self.click(self.el_popup_jumping)
        except Exception as e:
            print(f'没有出现弹窗或其他原因：{e}')
        # 点击窗口化
        self.click(self.el_DappRoom_windowed)

    '''关闭dapp'''

    def dapp_close1(self):
        # 进入第一个部落
        self.click(self.el_club1)
        # 选择dapp房间
        self.click(self.el_choose_DappRoom)
        # 弹窗点击确定
        try:
            self.click(self.el_popup_jumping)
        except Exception as e:
            print(f'没有出现弹窗或其他原因：{e}')
        self.click(self.el_DappRoom_close)

    '''最小化后再打开全屏'''

    def dapp_blow_up(self):
        # 先最小化
        self.dapp_windowed()
        # 放大到全屏
        self.click(self.el_DappWindowed_BlowUp)

    '''关闭dapp小窗'''

    def dapp_close2(self):
        # 先最小化
        self.dapp_windowed()
        # 关闭dapp窗口
        self.click(self.el_DappWindowed_Close)
