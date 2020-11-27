#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    author=xiangwei
    data=2020/03/31
"""
from Log.log import Log
from Page.register import Register
from Base.base import Base
from Base.init_driver import InitDriver
from util.get_data import GetData
from Config.readconfig import ReadConfig
import unittest,ddt,time
register_filename=r'F:\xw\example\web_projrct\Config\register_data.xls'
get_data=GetData(register_filename)
result_data =get_data.get_data()
@ddt.ddt
class TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.log=Log()
        cls.driver=InitDriver()
        cls.base=Base(cls.driver)
        cls.register=Register(cls.driver)
        read_config=ReadConfig(r'F:\xw\example\web_projrct\Config\platform.ini','URL')
        reigster_url=read_config.get_value('register_url')
        try:
            cls.log.info('开始注册测试')
            cls.log.info('开始打开注册网页')
            cls.driver.get(reigster_url)
            cls.driver.implicitly_wait(30)
            cls.log.info('打开注册网页成功')
        except Exception as e:
            cls.log.info('打开注册网页失败')
            raise e
    @ddt.data(*result_data)
    def test_register(self,data):
        self.log.info('开始第%s次注册测试'%data['序号'])
        self.log.info('输入注册邮箱、用户名、密码并点击注册')
        self.register.register(data['email'],data['user'],data['password'])
        try:
            self.log.info('开始断言')
            self.assertEqual(self.base.find_element(eval(data['error_element'])).text,data['result'])
            self.log.info('断言成功')
            self.log.info('开始第%s次注册测试成功' % data['序号'])
        except Exception as e:
            self.driver.get_screenshot_as_file(r'F:\xw\example\web_projrct\Config\screenshot\%s.png'%self._testMethodName)
            self.log.error('断言失败')
            self.log.info('开始第%s次注册测试失败' % data['序号'])
            raise e
        if int(data['序号'])<len(result_data):
            self.log.info('进入下一次登陆测试')
        else:
            self.log.info('注册测试结束')

        time.sleep(3)
    @classmethod
    def tearDownClass(cls):
        cls.log.info('关闭注册网页')
        cls.driver.close()
        cls.log.info('关闭完成')
if __name__=='__main__':
    unittest.main()


 