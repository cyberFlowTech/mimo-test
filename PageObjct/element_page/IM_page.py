from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from Base.base_page import BasePage


class IMPage(BasePage):
    # 底部消息table
    el_message_icon = (MobileBy.ACCESSIBILITY_ID,'message_unselected_icon_light')
    '''进入聊天室'''
    # 通讯录
    el_address_book = (MobileBy.XPATH,'//XCUIElementTypeStaticText[@name="通讯录"]')
    # 搜索框
    el_search = (MobileBy.CLASS_NAME,'XCUIElementTypeTextField')
    # 第六位好友
    el_choose_friend_six = (MobileBy.XPATH,'//XCUIElementTypeApplication[@name="Zapry"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[7]')
    # 我的群聊
    el_group_chart_list = (MobileBy.XPATH,'//XCUIElementTypeApplication[@name="Zapry"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeButton[2]')
    # 第一个群聊
    el_choose_group_first = (MobileBy.XPATH,'//XCUIElementTypeApplication[@name="Zapry"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[1]')
    # 消息输入框
    el_input_IM = (MobileBy.XPATH,
                   '//XCUIElementTypeApplication[@name="Zapry"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeTextView')
    # 发送消息按钮
    el_send_message = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="chat send message light"]')
    # +号更多按钮
    el_IM_more = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="chat more light"]')
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

    '''红包'''
    # 绑定钱包弹窗-立即设置
    el_wallet_popup_go = (By.XPATH, '//XCUIElementTypeButton[@name="立即设置"]')
    # 关闭钱包
    el_close_wallet = (MobileBy.XPATH, '//XCUIElementTypeNavigationBar[@name="RNSScreen"]/XCUIElementTypeOther[3]')
    # 选择其他币
    el_choose_coin = (MobileBy.ACCESSIBILITY_ID, 'red_bag_grayarrow_down')
    # 选择CIQI
    el_choose_CIQI = (MobileBy.ACCESSIBILITY_ID, 'CIQI, ALG L2(test), 837046934.1')
    # 金额
    el_sum = (MobileBy.XPATH,
              '//XCUIElementTypeApplication[@name="Zapry"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeTextField[1]')
    # 红包备注
    el_red_remark = (MobileBy.XPATH,
                 '//XCUIElementTypeApplication[@name="Zapry"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeTextField[2]')
    # 创建红包
    el_create_redpacket = (MobileBy.ACCESSIBILITY_ID, '创建红包')
    # 输入密码
    el_input_pwd = (By.XPATH,
                     '//XCUIElementTypeApplication[@name="Zapry"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeSecureTextField')
