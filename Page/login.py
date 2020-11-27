#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    author=xiangwei
    data=2020/03/31
"""
from Base.base import Base
from Config.readconfig import ReadConfig
class Login():
    def __init__(self,driver):
        self.read_config=ReadConfig(r'F:\xw\example\web_projrct\Config\el.ini','Login')
        self.base=Base(driver)
    def login(self,name,password):
        login_name=self.read_config.get_value('login_name')
        login_password=self.read_config.get_value('login_password')
        login_btn=self.read_config.get_value('login_btn')
        self.base.element_input(login_name,name)
        self.base.element_input(login_password,password)
        self.base.element_click(login_btn)
if __name__=='__main__':
    from selenium import webdriver
    driver=webdriver.Chrome()
    driver.get("http://www.5itest.cn/login")
    login=Login(driver)
    login.login('174@qq.com','12344')
 