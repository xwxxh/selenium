#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    author=xiangwei
    data=2020/04/01
"""
from Log.log import Log
from Page.login import Login
from Base.base import Base
from Base.init_driver import InitDriver
from util.get_data import GetData
import unittest,ddt,time
from Config.readconfig import ReadConfig
login_filename=r'F:\xw\example\web_projrct\Config\login_data.xls'
get_data=GetData(login_filename)
result_data =get_data.get_data()
@ddt.ddt
class TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.log=Log()
        cls.driver=InitDriver()
        cls.base=Base(cls.driver)
        cls.login=Login(cls.driver)
        read_config = ReadConfig(r'F:\xw\example\web_projrct\Config\platform.ini','URL')
        login_url = read_config.get_value('login_url')
        try:
            cls.log.info('开始登陆测试')
            cls.log.info('开始打开登陆网页')
            cls.driver.get(login_url)
            cls.driver.implicitly_wait(30)
            cls.log.info('打开登陆网页成功')
        except Exception as e:
            cls.log.info('打开登陆网页失败')
            raise e
    @ddt.data(*result_data)
    def test_login(self,data):
        self.log.info('开始第%s次登陆测试'%data['序号'])
        self.log.info('输入用户名及密码并点击登陆')
        self.login.login(data['user'],data['password'])
        self.log.info('开始断言')
        try:
            self.assertEqual(self.base.find_element(eval(data['error_element'])).text,data['result'])
            self.log.info('断言成功')
            self.log.info('开始第%s次登陆测试成功' % data['序号'])
        except Exception as e:
            self.driver.get_screenshot_as_file(r'F:\xw\example\web_projrct\Config\screenshot\%s.png'%self._testMethodName)
            self.log.info('断言失败')
            self.log.info('第%s次登陆测试失败' % data['序号'])
            raise e
        if int(data['序号'])<len(result_data):
            self.log.info('进入下一次登陆测试')
        else:
            self.log.info('登陆测试结束')
        time.sleep(3)
    @classmethod
    def tearDownClass(cls):
        cls.log.info('关闭登陆网页')
        cls.driver.close()
        cls.log.info('关闭登陆网页成功')
if __name__=='__main__':
    unittest.main()
 