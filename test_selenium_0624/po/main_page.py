# coding = 'utf-8'
# @作者：zeng
# @时间：2021/6/24
# @文件：main_page.py
#主页
from selenium import webdriver
from selenium.webdriver.common.by import By

from wechat_selenium_0624.po.basepage import BasePage
from wechat_selenium_0624.po.contact_page import ContactPage

#继承BasePage
class MainPage(BasePage):
    _CONTACT = (By.ID, "menu_contacts")

    # 跳转至通讯录页面
    def goto_contact(self):

        #self.driver.find_element_by_id("menu_contacts").click()
        self.find_and_click(*self._CONTACT)


        return ContactPage(self.driver)