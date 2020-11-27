#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    author=xiangwei
    data=2020/04/03
"""
import sys
from Log.log import Log
sys.path.append(r'F:\xw\example\SeleniumPython')
import HTMLTestRunner,unittest
from Sms.send_email import SendEmail
class RunMain():
    def __init__(self,case_path=None,report_path=None):
        if case_path:
            self.case_path=case_path
        else:
            self.case_path = r'F:\xw\example\web_projrct\Test_Case'
        if report_path:
            self.report_path=report_path
        else:
            self.report_path=r'F:\xw\example\web_projrct\report\result.html'
        self.log=Log()
        self.send=SendEmail()
    def run_all_case(self):
        case_path=r'F:\xw\example\web_projrct\Test_Case'
        discover=unittest.defaultTestLoader.discover(case_path,pattern='test*.py',top_level_dir=None)
        return discover
    def run_report(self):
        fp=open(self.report_path,'wb')
        runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='快乐学习网注册登陆测试报告',description='用例执行情况')
        runner.run(self.run_all_case())
        fp.close()
        try:
            self.log.info('发送邮件')
            self.send.send_main()
            self.log.info('发送邮件成功')
        except Exception as e:
            self.log.info('发送邮件失败：%s'%e)
if __name__=='__main__':
    run=RunMain()
    run.run_report()
