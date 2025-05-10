import os
from appium import webdriver
from appium.options.ios import XCUITestOptions
from requests import options
from common.data_util import readYaml

# 回到根目录
rootpath = os.path.abspath(os.path.dirname(__file__))
# yaml文件的绝对路径
path = os.path.join(rootpath, 'config/config.yaml')
# 使用redYaml方法拿到数据
data = readYaml(path)
# iOS参数
ios_caps={
  "platformName": "iOS", # 被测手机平台：Android/iOS
  "platformVersion": "17.5.1",# 手机iOS版本
  "deviceName": "iPhone 12", # 设备名，安卓手机可以随意填写
  "bundleId": "com.mimo.cyberflow.test",  # 启动APP Package名称
  # appActivity: .ui.splash.SplashActivity  # 启动Activity名称
  # unicodeKeyboard: True  # 使用自带输入法，输入中文时填True
  # resetKeyboard: True  # 执行完程序恢复原来输入法
  # noReset: True  # 不要重置App，如果为False的话，执行完脚本后，app的数据会清空，比如你原本登录了，执行完脚本后就退出登录了
  # newCommandTimeout: 6000  # 超时时间可以设置久一些，太短，用例比较多会报错
  "automationName": "XCUITest",  # 自动化测试引擎 ，默认Appium
  "udid": "00008101-000B38942E78001E" # ios手机的udid
}

# 连接Appium Server，初始化自动化环境
driver = webdriver.Remote('http://localhost:4723/wd/hub', data['ios_caps'])

# options = XCUITestOptions()
# options.platformName = "iOS"
# options.platformVersion = "17.5.1"
# options.deviceName = "iPhone 12" # 设备名，安卓手机可以随意填写
# options.bundleId = "com.mimo.cyberflow.test"  # 启动APP Package名称
# options.automationName = "XCUITest", # 自动化测试引擎 ，默认Appium
# options.udid = "00008101-000B38942E78001E" # ios手机的udid
# driver = webdriver.Remote('http://localhost:4723/wd/hub', options=options)