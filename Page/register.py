
#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    author=xiangwei
    data=2020/03/31
"""
from Base.base import Base
from Config.readconfig import ReadConfig
from util.get_code import GetCode
class Register():
    def __init__(self,driver):
        self.base=Base(driver)
        self.read_config=ReadConfig(r'F:\xw\example\web_projrct\Config\el.ini','Register')
        self.getcode=GetCode(driver)
#注册
    def register(self,email,user,password):

        register_email = self.read_config.get_value('register_email')
        register_name = self.read_config.get_value('register_name')
        register_password = self.read_config.get_value('register_password')
        register_input_code = self.read_config.get_value('register_input_code')
        register_get_code = self.read_config.get_value('register_get_code')
        register_btn = self.read_config.get_value('register_btn')
        self.base.element_input(register_email,email)
        self.base.element_input(register_name,user)
        self.base.element_input(register_password,password)		
        code=self.getcode.get_code(register_get_code)
        self.base.element_input(register_input_code,code)
        self.base.element_click(register_btn)
if __name__=='__main__':
    from selenium import webdriver
    driver=webdriver.Chrome()
    driver.get("http://www.5itest.cn/register")
    regist=Register(driver)
    #regist.get_el()
    regist.register('174@qq.com','12344','23456')


 