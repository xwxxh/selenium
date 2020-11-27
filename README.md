自主学习自动化测试框架
该框架采用python+selenium+excel+ddt+HTMLTestRunner+Email方式，目前只有注册和登陆

第一步：init__driver.py 实例化driver

第二步：base.py 封装定位方法和操作(点击，输入，删除...等等)

第三步：将配置参数和定位数据放置在ini文件中，通过configparser模块才获取

第四步：通过pytesseract模块来识别验证码并输入

第五步：封装页面注册

第六步：封装登陆页面

第七步：通过xlrd模块获取Excel中内容，用于注册或登陆的ddt数据驱动

第八步：封装注册测试方法，采用ddt数据驱动

第九步：封装登陆测试方法，采用ddt数据驱动

第十步：封装邮件发送，MIMEMultipart模块发送附件，MIMEText模块发送正文

第十一步：封装主程序，HTMLTestRunner模块生成html测试报告

同时还可以封装日志模块logging，便于中途使用
123456789