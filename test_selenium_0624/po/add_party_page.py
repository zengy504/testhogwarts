# coding = 'utf-8'
# @作者：zeng
# @时间：2021/6/24
# @文件：test_xxx.py
#添加部门详情页
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

from wechat_selenium_0624.po.basepage import BasePage


class AddPartyPage(BasePage):
    _PARTYNAME = (By.CSS_SELECTOR, ".inputDlg_item .ww_inputText")
    _PARTY = (By.CSS_SELECTOR, ".js_toggle_party_list")
    _PARTYCHILD = (By.XPATH, '//*[@id="1688850148092060"]/div')
    _SAVE = (By.CSS_SELECTOR, ".qui_btn.ww_btn.ww_btn_Blue")

    # 添加部门信息
    def edit_party(self,name):
        from wechat_selenium_0624.po.contact_page import ContactPage
        sleep(2)
        self.find(*self._PARTYNAME).send_keys(name)
        self.find_and_click(*self._PARTY)
        self.find_and_click(*self._PARTYCHILD)
        self.find_and_click(*self._SAVE)

        return ContactPage(self.driver)