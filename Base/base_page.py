from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    # 元素定位
    def locator(self, locator):
        return self.driver.find_element(*locator)

    # 输入
    def input(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    # 点击
    def click(self, locator):
        self.driver.find_element(*locator).click()

    # 滑动
    def swipe(self, start_x, start_y, end_x, end_y, duration=0):
        # 获取屏幕尺寸
        window_size = self.driver.window_size()
        x = window_size["width"]
        y = window_size["height"]
        touch_move = self.driver.swipe(start_x=x * start_x,
                                       start_y=y * start_y,
                                       end_x=x * end_x,
                                       end_y=y * end_y,
                                       duration=duration)
        return touch_move

    # 左滑
    def left_slide(self):
        self.driver.swipe(345, 298, 80, 298)

    # 右滑
    def right_slide(self):
        self.driver.swipe(2, 404, 263, 404)

    # 上滑
    def up_slide(self):
        self.driver.swipe(111, 641, 111, 209)

    # 下拉
    def down_slide(self):
        self.driver.swipe(111, 209, 111, 641)

    # 长按
    def long_press(self,element, duration_ms=2000):
        """
        执行长按操作
        :param element: 要长按的元素
        :param duration_ms: 长按持续时间(毫秒)
        """
        action = TouchAction(self.driver)
        action.long_press(element, duration=duration_ms).release().perform()

    # 单点
    def press(self,x, y, duration_ms=100):
        """
        通过坐标执行点击操作
        :param x: 横坐标
        :param y: 纵坐标
        :param duration_ms: 点击持续时间(毫秒)
        """
        action = TouchAction(self.driver)
        action.press(x=x, y=y).wait(duration_ms).release().perform()