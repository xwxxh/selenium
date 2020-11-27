#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    author=xiangwei
    data=2020/04/03
"""
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import  MIMEText
from Config.readconfig import ReadConfig
class SendEmail():
    def __init__(self):
        self.read_config=ReadConfig(r'F:\xw\example\web_projrct\Config\sms.ini','email')
    def send_email(self,path,text,subject):
        sender=self.read_config.get_value('sender_username')
        password=self.read_config.get_value('sender_password')
        smtpserver=self.read_config.get_value('smtpserver')
        receiver_list=self.read_config.get_value('receiver_list')
        msg=MIMEMultipart()
        msg['From']=sender
        msg['To']=','.join(receiver_list)
        msg['Subject']=subject
        with open(path,'rb') as fp:
            content=fp.read()
        body=MIMEText(text,'plain','utf-8')
        msg.attach(body)
        att=MIMEText(content,'base4','utf-8')
        att["Content-Type"] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        att["Content-Disposition"] = 'attachment; filename="result.html"'
        msg.attach(att)
        smtp=smtplib.SMTP()
        smtp.connect(smtpserver)
        smtp.login(sender,password)
        smtp.sendmail(sender,receiver_list,msg.as_string())
        smtp.close()
    def send_main(self):
        path=r'F:\xw\example\web_projrct\report\result.html'
        subject='快乐学习网注册登陆测试报告'
        text='快乐学习网注册登陆测试报告,请查收，如有疑问请及时联系'
        self.send_email(path,text,subject)



 