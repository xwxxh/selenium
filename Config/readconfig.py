#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    author=xiangwei
    data=2020/3/30
"""
import configparser,os
class ReadConfig():
    def __init__(self,filename,node):
        self.filename=filename
        self.node=node
        self.cf=self.load_ini()
    #加载ini文件
    def load_ini(self):
        cf=configparser.ConfigParser()
        cf.read(self.filename)
        return cf
    #获取元素信息：例如：('id','register_email') #eval:将获取到的字符串转为元组
    def get_value(self,key):

        data=eval(self.cf.get(self.node,key))
        return data
if __name__=='__main__':
    readini=ReadConfig(r'F:\xw\example\web_projrct\Config\el.ini','Register')
    #print(type(readini.get_value('register_url')))
    print(readini.get_value('register_email'))