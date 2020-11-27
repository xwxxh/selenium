#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    author=xiangwei
    data=2020/03/30
"""
import pytesseract
from PIL import Image
from Base.base import Base
class GetCode():
    def __init__(self,driver,filename=None):
        self.driver=driver
        if filename:
            self.filename=filename
        else:
            self.filename=r'F:\xw\example\web_projrct\Config\code.png'
    #获取验证码元素
    def get_code_el(self,loc):
        self.base = Base(self.driver)
        el=self.base.find_element(loc)
        return el
    #获取验证码并保存在filename中
    def get_code_image(self,loc):
        self.driver.save_screenshot(self.filename)
        #验证码尺寸
        size=self.get_code_el(loc).size
        width=size['width']
        height=size['height']
        #验证码坐标
        location=self.get_code_el(loc).location
        left=location['x']
        top=location['y']
        right=left+width
        bottom=top+height
        im=Image.open(self.filename)
        #按坐标裁剪，图形内只剩验证码
        im=im.crop((left,top,right,bottom))
        im.save(self.filename)
        return self.filename
    #解析验证码
    def get_code(self,loc):
        filename=self.get_code_image(loc)
        image=Image.open(filename)
        #验证码的图片模式为RGBA，是无法分配调色盘给透明通道的。更换为RGB模式
        image = image.convert('RGB')
        text=pytesseract.image_to_string(image)
        return text
if __name__=="__main__":
    from selenium import webdriver
    driver=webdriver.Chrome()
    driver.get("https://so.gushiwen.org/user/login.aspx")
    getcode=GetCode(driver)
    print(getcode.get_code(('id','imgCode')))