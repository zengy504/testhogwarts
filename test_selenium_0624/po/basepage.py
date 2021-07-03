# coding = 'utf-8'
# @作者：zeng
# @时间：2021/6/24
# @文件：basepage.py
#封装实例化代码
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver_base: WebDriver = None):
        # 当入参driver_base为空时，即第一次访问时为空
        # 避免driver重复初始化
        if driver_base is None:
            opt = webdriver.ChromeOptions()
            opt.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=opt)
            self.driver.implicitly_wait(10)
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
            print("实例化driver")
        else:
            #使用传进来的driver_base
            self.driver = driver_base

    #封装定位元素方法
    def find(self, by, locator):
        ele = self.driver.find_element(by, locator)
        return ele

    def finds(self, by, locator):
        eles = self.driver.find_elements(by, locator)
        return eles

    def find_and_click(self, by, locator):
        ele = self.driver.find_element(by, locator)
        ele.click()

    #封装等待方法,locator:元素
    def wait_for_click(self, locator, timeout=10):
        #类型注解
        element: WebElement = WebDriverWait(self.driver,timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()
        return element

    def close_driver(self):
        self.driver.close()

