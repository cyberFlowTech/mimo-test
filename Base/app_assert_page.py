from selenium.common import NoSuchElementException

class AppAssertPage:

    def __init__(self,driver):
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