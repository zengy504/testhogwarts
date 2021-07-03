# coding = 'utf-8'
# @作者：zeng
# @时间：2021/6/24
# @文件：add_member_page.py
#添加成员详情页
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

from wechat_selenium_0624.po.basepage import BasePage


class AddMemberPage(BasePage):
    _NAME = (By.ID, "username")
    _ACCTID = (By.ID, "memberAdd_acctid")
    _PHONE = (By.ID, "memberAdd_phone")
    _SAVE = (By.CSS_SELECTOR, ".js_btn_save")

    # 添加成员信息点击保存跳转到通讯录页面
    def edit_member(self,name,contact_id,phone):
        #局部导入，解决循环导入问题
        from wechat_selenium_0624.po.contact_page import ContactPage

        sleep(3)
        # self.driver.find_element_by_id("username").send_keys("江1")
        # self.driver.find_element_by_id("memberAdd_acctid").send_keys("jiang1")
        # self.driver.find_element_by_id("memberAdd_phone").send_keys("13800010001")
        # self.driver.find_element_by_css_selector(".js_btn_save").click()
        self.find(*self._NAME).send_keys(name)
        self.find(*self._ACCTID).send_keys(contact_id)
        self.find(*self._PHONE).send_keys(phone)
        self.find_and_click(*self._SAVE)

        return ContactPage(self.driver)