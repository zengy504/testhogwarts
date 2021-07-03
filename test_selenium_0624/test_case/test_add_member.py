# coding = 'utf-8'
# @作者：zeng
# @时间：2021/6/24
# @文件：test_xxx.py
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

    # def setup(self):
    #     self.main = MainPage()
    #
    # def teardown(self):
    #     return True


    # 获取配置文件路径
    curPath = os.path.abspath(os.path.dirname(__file__))
    file_yaml = os.path.abspath(os.path.dirname(curPath) + os.path.sep + "data/member.yaml")
    @pytest.mark.parametrize("name,contact_id,phone",yaml.safe_load(open(file_yaml,encoding="UTF-8")))
    def test_add_member(self,name,contact_id,phone):
        #链式调用
        result = self.main.goto_contact().click_add_member().edit_member(name,contact_id,phone).get_member_name()
        print("result:",result)
        assert name in result
