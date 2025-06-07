from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from Base.base_page import BasePage


class IMPage(BasePage):
    '''消息tab'''
    # 底部“消息”table
    el_message_icon = (MobileBy.ACCESSIBILITY_ID, 'message_unselected_icon_light')
    # +号
    el_add = (MobileBy.ACCESSIBILITY_ID, 'navigation add x24')
    # 发起群聊
    el_create_group = (MobileBy.ACCESSIBILITY_ID, '发起群聊')
    # 通讯录搜索
    el_address_search = (MobileBy.CLASS_NAME, 'XCUIElementTypeTextField')
    # 键盘上的”搜索“按钮
    el_search_keyboard = (MobileBy.ACCESSIBILITY_ID, 'Search')
    # 好友203
    el_friend_203 = MobileBy.ACCESSIBILITY_ID, '好友成203(203)'
    # 好友202
    el_friend_202 = MobileBy.ACCESSIBILITY_ID, 'new202'
    # 第一个item
    el_item_first = (MobileBy.XPATH,'//XCUIElementTypeApplication[@name="Zapry"]/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[1]')

    '''通讯录'''
    # 通讯录
    el_address_book = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="通讯录"]')
    # 搜索框
    el_search = (MobileBy.CLASS_NAME, 'XCUIElementTypeTextField')
    # 第六位好友
    el_choose_friend_six = (MobileBy.XPATH,
                            '//XCUIElementTypeApplication[@name="Zapry"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[7]')
    # 我的群聊
    el_group_chart_list = (MobileBy.XPATH,
                           '//XCUIElementTypeApplication[@name="Zapry"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeButton[2]')
    # 群聊"1111"
    el_group_1111 = (MobileBy.ACCESSIBILITY_ID, '1111')

    '''聊天室'''
    # 消息输入框
    el_input_IM = (MobileBy.XPATH,
                   '//XCUIElementTypeApplication[@name="Zapry"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeTextView')
    # 发送消息按钮
    el_send_message = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="chat send message light"]')
    # +号更多按钮
    el_IM_more = (By.XPATH, '//XCUIElementTypeButton[@name="chat more light"]')
    # 相册
    el_photo_choose = (MobileBy.ACCESSIBILITY_ID, 'chat_more_album_light')
    # 拍照
    el_take_a_photo = (MobileBy.ACCESSIBILITY_ID, 'chat_more_camera_light')
    # 语音通话
    el_voice_communication = (MobileBy.ACCESSIBILITY_ID, 'chat_more_voice_light')
    # 红包
    el_red_packet = (MobileBy.ACCESSIBILITY_ID, 'chat_more_redpacket_light')
    # 转账
    el_transfer_accounts = (MobileBy.ACCESSIBILITY_ID, 'chat_more_transfer_light')
    # 个人名片
    el_personal_card = (MobileBy.ACCESSIBILITY_ID, 'chat_more_personal_card_light')
    # 文件
    el_document = (MobileBy.ACCESSIBILITY_ID, 'chat_more_document_light')
    # 选择图片
    el_picture_choose = (MobileBy.XPATH,
                         '//XCUIElementTypeApplication[@name="Zapry"]/XCUIElementTypeWindow/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[4]/XCUIElementTypeOther/XCUIElementTypeButton')
    # 发送图片
    el_send_picture = (MobileBy.ACCESSIBILITY_ID, '发送(1)')
    # 选择视频
    el_video_choice = (MobileBy.XPATH,
                       '(//XCUIElementTypeImage[@name="/var/containers/Bundle/Application/7024A092-04C5-4391-8650-52A234FC16EB/Zapry.app/TZImagePickerController.bundle/photo_def_photoPickerVc@2x.png"])[2]')

    '''发红包'''
    # 绑定钱包弹窗-立即设置
    el_wallet_popup_go = (By.XPATH, '//XCUIElementTypeButton[@name="立即设置"]')
    # 关闭钱包
    el_close_wallet = (MobileBy.XPATH, '//XCUIElementTypeNavigationBar[@name="RNSScreen"]/XCUIElementTypeOther[3]')
    # 选择红包类型
    el_choose_redpacket_type = (MobileBy.ACCESSIBILITY_ID, 'red_bag_arrow_down')
    # 拼手气红包
    el_luck_redpacket = (MobileBy.XPATH, '(//XCUIElementTypeButton[@name="拼手气红包"])[2]')
    # 普通红包
    el_common_redpacket = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="普通红包"]')
    # 群聊红包个数
    el_group_number = (By.XPATH,
                       '//XCUIElementTypeApplication[@name="Zapry"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeTextField[1]')
    # 房间红包个数
    el_channel_number = (By.XPATH,
                         '//XCUIElementTypeApplication[@name="Zapry"]/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeTextField[1]')
    # 选择其他币
    el_choose_coin = (MobileBy.ACCESSIBILITY_ID, 'red_bag_grayarrow_down')
    # 选择ALG
    el_choose_ALG = (MobileBy.ACCESSIBILITY_ID, 'ALG')
    # 选择CIQI
    el_choose_CIQI = (MobileBy.ACCESSIBILITY_ID, 'CIQI')
    # 单聊红包金额
    el_solo_sum = (MobileBy.XPATH,
                   '//XCUIElementTypeApplication[@name="Zapry"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeTextField[1]')
    # 群聊、频道红包金额
    el_channel_sum = (MobileBy.XPATH,
                      '//XCUIElementTypeApplication[@name="Zapry"]/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeTextField[2]')
    # 单聊红包备注
    el_solo_remark = (MobileBy.XPATH,
                      '//XCUIElementTypeApplication[@name="Zapry"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeTextField[2]')
    # 群聊、频道红包备注
    el_channel_remark = (MobileBy.XPATH,
                         '//XCUIElementTypeApplication[@name="Zapry"]/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeTextField[3]')
    # 创建红包
    el_create_redpacket = (MobileBy.ACCESSIBILITY_ID, '创建红包')
    # 输入密码
    el_input_pwd = (By.XPATH,
                    '//XCUIElementTypeApplication[@name="Zapry"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeSecureTextField')
    '''领红包'''
    # 单聊自动化ALG红包
    el_solo_ALG = MobileBy.ACCESSIBILITY_ID,'单聊自动化ALG红包'
    # 单聊自动化CIQI红包
    el_solo_CIQI = MobileBy.ACCESSIBILITY_ID,'单聊自动化CIQI红包'
    # 群聊自动化CIQI拼手气红包
    el_group_lucky_CIQI = MobileBy.ACCESSIBILITY_ID, '群聊自动化CIQI拼手气红包'
    # 群聊自动化ALG普通红包
    el_group_common_ALG = MobileBy.ACCESSIBILITY_ID, '群聊自动化ALG普通红包'
    # 频道自动化ALG拼手气红包
    el_channel_lucky_ALG = MobileBy.ACCESSIBILITY_ID, '频道自动化ALG拼手气红包'
    # 频道自动化CIQI普通红包
    el_channel_common_CIQI = MobileBy.ACCESSIBILITY_ID, '频道自动化CIQI普通红包'
    # 开红包
    el_open_red_package = MobileBy.ACCESSIBILITY_ID,'red_bag_open_button'

    '''群聊设置'''
    # 进入聊天设置
    el_chart_setting = (MobileBy.XPATH,'//XCUIElementTypeButton[@name="chat setting light"]')
    # 返回
    el_setting_go_back = (MobileBy.ACCESSIBILITY_ID,'返回')
    # 拉好友建群
    el_chart_setting_add = (MobileBy.ACCESSIBILITY_ID,'chat setting add')
    # 建群选择第一个好友
    el_add_first = (MobileBy.XPATH,'(//XCUIElementTypeButton[@name="group user unselect"])[1]')
    # 建群选择第二个好友
    el_add_second = (MobileBy.XPATH, '(//XCUIElementTypeButton[@name="group user unselect"])[2]')
    # 拉人选择我第五位好友
    el_add_five = (MobileBy.XPATH,'(//XCUIElementTypeButton[@name="group user unselect"])[5]')
    # 确认建群
    el_add_done1 = (MobileBy.XPATH,'//XCUIElementTypeStaticText[@name="完成(1/9)"]')
    el_add_done2 = (MobileBy.XPATH,'//XCUIElementTypeButton[@name="完成(2/9)"]')
    # 群聊名称
    el_setting_group_name = (MobileBy.ACCESSIBILITY_ID,'群聊名称')
    # 清除名称
    el_setting_clear_name = (MobileBy.ACCESSIBILITY_ID,'清除文本')
    # 输入群聊名称
    el_setting_set_name = (MobileBy.CLASS_NAME,'XCUIElementTypeTextField')
    # 保存群聊名称
    el_setting_save_name = (MobileBy.XPATH,'//XCUIElementTypeStaticText[@name="保存"]')
