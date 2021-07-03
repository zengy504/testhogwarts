# coding = 'utf-8'
# @作者：zeng
# @时间：2021/6/24
# @文件：test_contacts.py
import os
import pytest
import yaml
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestWebchat():
    def setup_method(self):
        self.driver = webdriver.Chrome()

    def teardown_method(self):
        self.driver.quit()

def test_login():
        opt = webdriver.ChromeOptions()
        opt.debugger_address = "127.0.0.1:9222"
        driver = webdriver.Chrome(options=opt)
        driver.get("https://work.weixin.qq.com/wework_admin/frame")
        driver.find_element_by_id("menu_contacts").click()
        #获取cookie
        cookies = driver.get_cookies()
        # 获取配置文件路径
        curPath = os.path.abspath(os.path.dirname(__file__))
        print("curPath:",curPath)
        file_yaml = os.path.abspath(os.path.dirname(curPath) + os.path.sep + "data/data.yaml")
        print("file_yaml:", file_yaml)
        # 将cookies存入yaml文件中
        with open(file_yaml, "w", encoding="UTF-8") as f:
            yaml.dump(cookies, f)
        # 获取cookie信息
        # print(driver.get_cookies())

#获取cookie免登陆,从yaml文件中读取cookie
def test_weixin_cookie():
    driver = webdriver.Chrome()
    driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
    # 最大化浏览器窗口
    driver.maximize_window()
    # 获取配置文件路径
    curPath = os.path.abspath(os.path.dirname(__file__))
    file_yaml = os.path.abspath(os.path.dirname(curPath) + os.path.sep + "data/data.yaml")
    #读取yaml文件内容
    with open(file_yaml, "r",  encoding="UTF-8") as f:
        yaml_data = yaml.safe_load(f)
    for cookie in yaml_data:
        driver.add_cookie(cookie)

    driver.get("https://work.weixin.qq.com/wework_admin/frame")

    #打开通讯录页面
    driver.find_element_by_id("menu_contacts").click()

    # 显示等待10s可点击状态
    ele = (By.CSS_SELECTOR,".ww_operationBar .js_add_member")
    WebDriverWait(driver,10).until(EC.element_to_be_clickable(ele))
    # element = WebDriverWait(driver, 5, 0.5).until(
    #     EC.visibility_of_element_located((By.CSS_SELECTOR, ".ww_operationBar .js_add_member"))
    # )

    #点击添加成员按钮
    driver.find_element_by_css_selector(".ww_operationBar .js_add_member").click()
    sleep(2)

    driver.find_element_by_id("username").send_keys("林5")
    driver.find_element_by_id("memberAdd_acctid").send_keys("lin5")
    driver.find_element_by_id("memberAdd_phone").send_keys("13800000005")
    driver.find_element_by_css_selector(".js_btn_save").click()
    sleep(5)
    # 断言
    eles = driver.find_elements_by_css_selector(".member_colRight_memberTable_td:nth-child(2)")
    for x in eles:
        if x.get_attribute("title") == "林5":
            return True

    sleep(2)
    driver.quit()

def test_add_contacts():
    opt = webdriver.ChromeOptions()
    opt.debugger_address = "127.0.0.1:9222"
    driver = webdriver.Chrome(options=opt)
    driver.get("https://work.weixin.qq.com/wework_admin/frame")
    driver.find_element_by_id("menu_contacts").click()
    # 显示等待10s可点击状态
    ele = (By.CSS_SELECTOR, ".ww_operationBar .js_add_member")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(ele))
    # 点击添加成员按钮
    driver.find_element_by_css_selector(".ww_operationBar .js_add_member").click()
    sleep(3)

    driver.find_element_by_id("username").send_keys("林7")
    driver.find_element_by_id("memberAdd_acctid").send_keys("lin7")
    driver.find_element_by_id("memberAdd_phone").send_keys("13800000007")
    driver.find_element_by_css_selector(".js_btn_save").click()
    sleep(5)
    # 断言
    eles = driver.find_elements_by_css_selector(".member_colRight_memberTable_td:nth-child(2)")
    for x in eles:
        if x.get_attribute("title") == "林7":
            return True