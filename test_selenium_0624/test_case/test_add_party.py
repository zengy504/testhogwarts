# coding = 'utf-8'
# @作者：zeng
# @时间：2021/6/29
# @文件：test_add_party.py
import pytest
import yaml
import os

from wechat_selenium_0624.po.main_page import MainPage


class TestAddMember:
    def setup_class(self):
        self.main = MainPage()

    def teardown_class(self):
        return True
       # self.main.close_driver()

    @pytest.mark.parametrize("name",["test1"])
    def test_add_party(self,name):
        #链式调用
        result = self.main.goto_contact().click_add_party().edit_party(name).get_party_name()
        print("result:",result)
        assert name in result
