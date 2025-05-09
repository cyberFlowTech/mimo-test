from appium.webdriver.common.mobileby import MobileBy

from Base.base_page import BasePage


class IMPage(BasePage):
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
    el_picture_choose = (MobileBy.XPATH,'//XCUIElementTypeApplication[@name="Zapry"]/XCUIElementTypeWindow/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[4]/XCUIElementTypeOther/XCUIElementTypeButton')
    # 发送图片
    el_send_picture = (MobileBy.ACCESSIBILITY_ID, '发送(1)')
    # 选择视频
    el_video_choice = (MobileBy.XPATH,'(//XCUIElementTypeImage[@name="/var/containers/Bundle/Application/7024A092-04C5-4391-8650-52A234FC16EB/Zapry.app/TZImagePickerController.bundle/photo_def_photoPickerVc@2x.png"])[2]')


