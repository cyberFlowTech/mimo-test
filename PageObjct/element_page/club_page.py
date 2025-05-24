from appium.webdriver.common.mobileby import MobileBy
from Base.base_page import BasePage


class ClubPage(BasePage):
    """元素定位"""

    '''创建部落'''
    el_icon = (MobileBy.ACCESSIBILITY_ID, "tribe_add_light")
    # +号浮层中的创建普通部落
    el_create = (MobileBy.ACCESSIBILITY_ID, "tribe_create_banner")
    # +号浮层中的创建订阅部落
    el_create_subscribe = (MobileBy.ACCESSIBILITY_ID, "tribe_create_subscribe_banner")
    # 添加头像
    el_photo = (MobileBy.XPATH,
                "//XCUIElementTypeApplication[@name='Zapry']/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton")
    # 选择照片
    el_choose = (MobileBy.XPATH,
                 "//XCUIElementTypeApplication[@name='Zapry']/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[8]/XCUIElementTypeOther/XCUIElementTypeImage")
    # 完成
    el_finish = (MobileBy.XPATH, '(//XCUIElementTypeStaticText[@name="完成"])[2]')
    # 裁剪完成
    el_tailor = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="完成"]')
    # 名字输入框
    el_name = (MobileBy.CLASS_NAME, 'XCUIElementTypeTextField')
    # 创建普通部落的icon
    el_create_club = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="创建部落"]')
    # 创建订阅部落的下一步
    el_create_next = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="下一步"]')

    '''部落创建完成后的后续操作'''
    # 跳过
    el_skip = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="跳过"]')
    # 邀请你的好友
    el_invite = (MobileBy.XPATH,
                 '//XCUIElementTypeApplication[@name="Zapry"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeTable/XCUIElementTypeCell[2]')
    # 去设置欢迎页
    el_Wellcome = (MobileBy.XPATH,
                   '//XCUIElementTypeApplication[@name="Zapry"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeTable/XCUIElementTypeCell[3]')
    # 查看部落管理
    el_view_manage = (MobileBy.XPATH,
                      '//XCUIElementTypeApplication[@name="Zapry"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeTable/XCUIElementTypeCell[4]')
    # 查看部落数据
    el_view_data = (MobileBy.XPATH,
                    '//XCUIElementTypeApplication[@name="Zapry"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeTable/XCUIElementTypeCell[5]')
    # 发布一则动态
    el_active = (MobileBy.XPATH,
                 '//XCUIElementTypeApplication[@name="Zapry"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeTable/XCUIElementTypeCell[6]')
    # 跳过这些步骤
    el_skip_all = (MobileBy.ACCESSIBILITY_ID, '跳过这些步骤')

    '''部落首页元素'''
    # 侧边栏由上至下第一个部落
    el_club1 = (MobileBy.XPATH,
                '//XCUIElementTypeApplication[@name="Zapry"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[1]/XCUIElementTypeOther/XCUIElementTypeImage')
    el_club2 = (MobileBy.XPATH,'//XCUIElementTypeApplication[@name="Zapry"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[2]/XCUIElementTypeOther/XCUIElementTypeImage')
    el_club3 = (MobileBy.XPATH,'//XCUIElementTypeApplication[@name="Zapry"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[3]/XCUIElementTypeOther/XCUIElementTypeImage')
    el_club4 = (MobileBy.XPATH,'//XCUIElementTypeApplication[@name="Zapry"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[4]/XCUIElementTypeOther/XCUIElementTypeImage')
    el_club5 = (MobileBy.XPATH,'//XCUIElementTypeApplication[@name="Zapry"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[5]/XCUIElementTypeOther/XCUIElementTypeImage')
    # 部落设置
    el_setting = (MobileBy.ACCESSIBILITY_ID, 'tribe setting light')
    # 分享二维码
    el_share = (MobileBy.ACCESSIBILITY_ID, 'tribe share light')
    # 部落内搜索聊天记录
    el_search = (MobileBy.ACCESSIBILITY_ID, 'tribe search light')
    # 部落社区
    el_community = (MobileBy.XPATH,
                    '//XCUIElementTypeApplication[@name="Zapry"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[1]')
    # 部落首页添加房间
    el_add_room = (MobileBy.XPATH, '(//XCUIElementTypeButton[@name="tribe detail add light"])[4]')

    '''分享部落二维码'''
    # 分享到IM--邀请好友
    el_invite_IM = (MobileBy.ACCESSIBILITY_ID, 'tribe_invite_circle_friend')

    '''选择聊天页面'''
    # #外层搜索输入框热区（热区：可点击热区）
    el_search_out = (MobileBy.XPATH,
                     '//XCUIElementTypeApplication[@name="Zapry"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeTextField')
    # 我的部落热区
    el_my_club = (MobileBy.XPATH,
                  '//XCUIElementTypeApplication[@name="Zapry"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[1]')
    # 我的联系人热区
    el_my_contacts = (MobileBy.XPATH,
                      '//XCUIElementTypeApplication[@name="Zapry"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[2]')
    # #我的群聊热区
    el_my_group = (MobileBy.XPATH,
                   '//XCUIElementTypeApplication[@name="Zapry"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[3]')
    # 联系人内搜索
    el_contacts_search = (MobileBy.XPATH,
                          '//XCUIElementTypeApplication[@name="Zapry"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeTextField[2]')

    '''分享到部落'''
    # 左侧往下第二个部落
    el_second_club = (MobileBy.XPATH,
                      '//XCUIElementTypeApplication[@name="Zapry"]/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell[2]/XCUIElementTypeOther/XCUIElementTypeImage')
    # 选择‘日常聊天’房间
    el_choose_chart_room = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="日常聊天"]')
    # 选择“聊天房间”
    el_choose_ChartRoom1 = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="聊天房间"]')
    # 选择“应用房间”房间
    el_choose_DappRoom = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="应用房间"]')
    # 点击‘完成’
    el_share_club_done = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="完成(1)"]')

    '''分享-搜索联系人'''
    # 搜索出来的item的名字
    el_first_name = (MobileBy.XPATH, '(//XCUIElementTypeStaticText[@name="204！"])[2]')
    # #我的联系人第一个item
    # el_first_item = (MobileBy.XPATH,'//XCUIElementTypeApplication[@name="Zapry"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[1]')
    # 确认
    el_confirm = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="确认(1/9)"]')
    # 聚合页点击完成
    el_share_done = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="完成(1/9)"]')

    '''分享到群聊'''
    # 群聊搜索输入框
    el_group_search = (MobileBy.XPATH,
                       '//XCUIElementTypeApplication[@name="Zapry"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeTextField[2]')
    # 选择第一个群聊
    el_share_group_first = (MobileBy.XPATH,
                             '//XCUIElementTypeApplication[@name="Zapry"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable[2]/XCUIElementTypeCell[1]')
    # 点击确认
    el_group_confirm = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="确认(1/9)"]')

    # 分享弹窗选择发送
    el_share_send = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="发送"]')

    '''发部落动态'''
    # 写动态按钮
    el_send_community = (MobileBy.ACCESSIBILITY_ID, 'tribe send community', 'discover post icon')
    # 标题
    el_head_title = (MobileBy.XPATH,
                     '//XCUIElementTypeApplication[@name="Zapry"]/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeTextView')
    # 正文
    el_body_text = (MobileBy.XPATH,
                    '//XCUIElementTypeApplication[@name="Zapry"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[2]/XCUIElementTypeTextView')
    # 发布按钮
    el_release = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="发布"]')

    '''创建房间'''
    # 创建普通房间
    el_chart_room = (MobileBy.XPATH,
                     '//XCUIElementTypeApplication[@name="Zapry"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[1]/XCUIElementTypeOther')
    # 房间名输入框
    el_chart_name = (MobileBy.CLASS_NAME, 'XCUIElementTypeTextField')
    # 立即创建
    el_create_button = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="立即创建"]')
    # 创建DAPP房间
    el_dapp_room = (MobileBy.XPATH,
                    '//XCUIElementTypeApplication[@name="Zapry"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[2]/XCUIElementTypeOther')
    # DAPP房间名输入框
    el_dapp_name = (MobileBy.XPATH,
                    '//XCUIElementTypeApplication[@name="Zapry"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeTextField')
    # 应用链接输入框
    el_dapp_link = (MobileBy.XPATH,
                    '//XCUIElementTypeApplication[@name="Zapry"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeTextField')
    # 应用介绍输入框
    el_dapp_text = (MobileBy.CLASS_NAME, 'XCUIElementTypeTextView')
    # 创建完成
    el_dapp_done = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="完成"]')
    # 进入聊天频道
    el_into_channel = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="日常聊天"]')

    '''聊天房间信息页'''
    # 进入房间信息
    el_chart_room_information = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="chat setting light"]')
    # 返回
    el_back = (MobileBy.ACCESSIBILITY_ID, '返回')
    # 全员禁言
    el_all_Shutup = (MobileBy.CLASS_NAME, 'XCUIElementTypeSwitch')
    # 消息免打扰
    el_message_disturb = (MobileBy.ACCESSIBILITY_ID, '消息免打扰')
    # 清空聊天消息
    el_clear_message = (MobileBy.ACCESSIBILITY_ID, '清空聊天记录')
    # 删除房间
    el_delete_room = (MobileBy.ACCESSIBILITY_ID, '删除房间')

    '''发布房间公告'''
    # 设置房间公告
    el_announce = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="房间公告"]')
    # 编辑公告
    el_announce_content = (MobileBy.CLASS_NAME, 'XCUIElementTypeTextView')
    # 发布
    el_announcement = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="发布"]')

    '''设置免打扰'''
    # 不允许通知
    el_no_disturb = (MobileBy.CLASS_NAME, '不允许通知')

    '''清空聊天记录'''
    # 清空弹窗，二次确认
    el_clear_popup = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="清空"]')

    '''删除房间'''
    # 删除弹窗，二次确认
    el_delete_popup = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="删除"]')
    '''应用房间相关'''
    # 未绑定钱包点击应用房间的弹窗
    el_popup_BindWallet = (MobileBy.XPATH,'//XCUIElementTypeButton[@name="立即添加"]')
    # 应用房间跳转提示
    el_popup_jumping = (MobileBy.XPATH,'//XCUIElementTypeButton[@name="确定"]')
    # 应用房间聊天气泡
    el_DappRoom_chart =(MobileBy.XPATH,'//XCUIElementTypeImage[@name="dapp_chat2"]')
    # 应用房间功能浮层
    el_DappRoom_util = (MobileBy.ACCESSIBILITY_ID,'dappMoreIcon')
    # dapp窗口化
    el_DappRoom_windowed = (MobileBy.ACCESSIBILITY_ID,'dappWindowedIcon')
    # 关闭dapp
    el_DappRoom_close = (MobileBy.ACCESSIBILITY_ID,'dappCloseIcon')
    # dapp窗口放大
    el_DappWindowed_BlowUp = (MobileBy.ACCESSIBILITY_ID,'windowedFullSize')
    # dapp窗口关闭
    el_DappWindowed_Close = (MobileBy.ACCESSIBILITY_ID,'windowedClosed')
    # 聊天
    el_dapp_chart2 = (MobileBy.ACCESSIBILITY_ID,'dapp chat')
    # 分享dapp
    el_dapp_share = (MobileBy.ACCESSIBILITY_ID,'dapp chat')




    '''创建钱包'''
    # 创建新钱包
    el_create_NewWallet = (MobileBy.XPATH, '//XCUIElementTypeOther[@name="创建新钱包"]')
    # 二次确认
    el_popup_NewWallet = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="创建新钱包"]')
    # 跳过生物识别
    el_recognition_skip = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="跳过"]')
    # 设置密码为“111111”
    el_PayPwd = (MobileBy.XPATH, '//XCUIElementTypeKey[@name="1"]')