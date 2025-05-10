import os

import pytest
from appium.webdriver.webdriver import WebDriver
from common.data_util import readYaml

class StartApp:
    def test_start_app(self):
        # 回到根目录
        rootpath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        # yaml文件的绝对路径
        path = os.path.join(rootpath, 'config/config.yaml')
        # 拿到数据
        data = readYaml(path)
        # 连接Appium Server，初始化自动化环境
        self.driver = WebDriver('http://localhost:4723/wd/hub', data['ios_caps'])

