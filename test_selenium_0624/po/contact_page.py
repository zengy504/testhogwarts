# coding = 'utf-8'
# @作者：zeng
# @时间：2021/6/24
# @文件：contact_page.py
#通讯录页面
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from wechat_selenium_0624.po.add_member_page import AddMemberPage
from wechat_selenium_0624.po.add_party_page import AddPartyPage
from wechat_selenium_0624.po.basepage import BasePage


class ContactPage(BasePage):
    _ADDMEMBER = (By.CSS_SELECTOR, ".ww_operationBar .js_add_member")
    _NAMES = (By.CSS_SELECTOR,".member_colRight_memberTable_td:nth-child(2)")
    # 点击 + 号
    _ADDPARTY = (By.CSS_SELECTOR, ".member_colLeft_top_addBtn")
    # 点击添加部门
    _CREATEPARTY = (By.CSS_SELECTOR, ".js_create_party")
    _PARTYNAMES = (By.CSS_SELECTOR, ".jstree-themeicon-custom")

    #点击添加成员
    def click_add_member(self):

        # 显示等待10s可点击状态
        #ele = (By.CSS_SELECTOR, ".ww_operationBar .js_add_member")
        #WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(ele))
        # 点击添加成员按钮
        #self.driver.find_element_by_css_selector(".ww_operationBar .js_add_member").click()
        self.wait_for_click(self._ADDMEMBER)


        return AddMemberPage(self.driver)

    #获取成员信息
    def get_member_name(self):
        sleep(5)

        name_list= []
        # 断言
        #eles = self.driver.find_elements_by_css_selector(".member_colRight_memberTable_td:nth-child(2)")
        eles = self.finds(*self._NAMES)
        for value in eles:
            name_list.append(value.get_attribute("title"))
        print("name_list:", name_list)
        return name_list

    # 点击添加部门
    def click_add_party(self):
        # 显示等待
        self.wait_for_click(self._ADDPARTY)
        self.wait_for_click(self._CREATEPARTY)
        return AddPartyPage(self.driver)

    # 获取部门信息
    def get_party_name(self):
        sleep(5)
        name_list = []
        # 断言
        eles = self.finds(*self._PARTYNAMES)
        for value in eles:
            name_list.append(value.get_attribute("title"))
        print("partyname_list:", name_list)
        return name_list