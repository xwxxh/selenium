#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    author=xiangwei
    data=2020/3/28
"""
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Base():
    def __init__(self,driver):
        self.driver=driver
    #元素定位
    def find_element(self,loc,timeout=10,interval=1):
        """
        :param timeout: 超时时间
        :param interval: 间隔时间
        :param loc: 元组 （'id','value'）
        """
        return WebDriverWait(self.driver,timeout,interval).until(EC.presence_of_element_located(loc))
    #定位一组元素
    def find_elements(self,loc,timeout=10,interval=1):
        return WebDriverWait(self.driver,timeout,interval).until(EC.presence_of_element_located(loc))
    #元素点击
    def element_click(self,loc):
        self.find_element(loc).click()
    #输入内容
    def element_input(self,loc,text):
        self.find_element(loc).clear()
        self.find_element(loc).send_keys(text)
    #获取属性值
    def get_attribute_value(self,loc,porp):
        self.find_element(loc).get_attribute(porp)

 