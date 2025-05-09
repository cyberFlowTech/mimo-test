from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from appium import webdriver


class WaitPage:
    def __init__(self, driver):
        self.driver = driver

    # 定义一个获取元素的方法
    def get_element(self,driver, *element):
        element = WebDriverWait(driver,10).until(EC.element_to_be_clickable(*element))
        return element

