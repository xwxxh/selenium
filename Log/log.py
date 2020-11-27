#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    author=xiangwei
    data=2020/04/03
"""
import logging,sys
class Log():
    def __init__(self):
        self.logger = logging.getLogger()
        self.format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s') #设置日志显示格式
    def __console(self,level,message):
        self.file_handler = logging.FileHandler(r"F:\xw\example\web_projrct\Log\log.txt",'a')#将日志发送到磁盘指定文件夹下
        self.file_handler.setFormatter(self.format)  # 通过setFormatter指定输出格式 （时间 等级 信息）格式
        self.file_handler.setLevel(logging.INFO)#磁盘文件输出最低日志等级
        self.console_handler = logging.StreamHandler(sys.stdout)#将日志输送到控制台
        self.console_handler.setFormatter(self.format) # 指定输出格式，也可以直接给formatter赋值self.console_handler.formatter=self.formatter
        self.logger.setLevel(logging.INFO) #设置控制台输送日志最低等级
        self.logger.addHandler(self.file_handler)     #添加一个输入文件夹下的处理器
        self.logger.addHandler(self.console_handler) #添加一个输入到控制台的处理器
        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
     # 这两行代码是为了避免日志输出重复问题
        self.logger.removeHandler(self.file_handler)
        self.logger.removeHandler(self.console_handler)
        #删除两个处理器haddle，若没上述两行，则每次调用__console都会添加一个处理器haddle，
        #就会重复一条日志，就会出现1条测试开始，2条输入密码，3条测试结束的重复日志
        self.file_handler.close()
    def debug(self,message):
        self.__console('debug', message)
    def info(self,message):
        self.__console('info', message)
    def warning(self,message):
        self.__console('warning', message)
    def error(self,message):
        self.__console('error', message)
if __name__ == "__main__":
    log = Log()
    log.info("---测试开始----")
    log.info("输入密码")
    log.warning("----测试结束----")

 