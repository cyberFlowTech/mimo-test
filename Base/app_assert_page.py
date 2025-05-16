from selenium.common import NoSuchElementException


class AppAssertPage:

    def __init__(self, driver):
        self.driver = driver

    def is_element_present(self, how, what):
        '''
        判断元素是否存在
        :param how: 定位方式
        :param what: 定位元素的属性值
        :return: True：代表元素存在， False：代表元素不存在
        '''
        try:
            self.driver.find_element(how, what)
            return True

        except NoSuchElementException:
            return False

    def is_element_displayed(self, how, what):
        '''
        判断元素是否可见
        :param how: 定位方式
        :param what: 定位元素的属性值
        :return: True：代表元素可见， False：代表元素不可见
        '''
        try:
            self.driver.find_element(how, what).is_displayed()
            return True
        except NoSuchElementException:
            return False

    def is_element_enabled(self, how, what):
        '''
        判断元素是否可输入
        :param how: 定位方式
        :param what: 定位元素的属性值
        :return: True：代表元素可输入， False：代表元素不可输入
        '''
        try:
            self.driver.find_element(how, what).is_enabled()
            return True
        except NoSuchElementException:
            return False

    def is_element_clickable(self, how, what):
        '''
        判断元素是否可点击
        :param how: 定位方式
        :param what: 定位元素的属性值
        :return: True：代表元素可点击， False：代表元素不可点击
        '''
        try:
            self.driver.find_element(how, what).is_clickable()
            return True
        except NoSuchElementException:
            return False
