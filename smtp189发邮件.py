#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication


# 1、发送普通邮件 2、发送带附件邮件 


def mail(receiver, subject, content, cc_list):
    my_sender = 'xxxx'    # 发件人邮箱账号
    my_pass = 'xxxx'    # 发件人邮箱密码
    msg = MIMEMultipart()
    msg['From'] = Header(my_sender, 'utf-8')  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
    msg['To'] = ','.join(receiver)              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
    msg['Cc'] = ",".join(cc_list)  #抄送
    msg['Subject'] = Header(subject, 'utf-8')     # 邮件的主题，也可以说是标题,'utf-8'

    text = MIMEText(content, 'plain', 'utf-8')
    msg.attach(text)

    server = smtplib.SMTP_SSL("smtp.chinatelecom.cn", 465, timeout=10)
    server.login(my_sender, my_pass)
    server.sendmail(my_sender, receiver, msg.as_string())


def mail_file(receiver, subject, content, address, cc_list):
    rename = address.split('\\')[-1]
    my_sender = 'xxxx'    # 发件人邮箱账号
    my_pass = 'xxxx'    # 发件人邮箱密码
    msg = MIMEMultipart()
    msg['From'] = my_sender  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
    msg['To'] =','.join(receiver)             # 括号里的对应收件人邮箱昵称、收件人邮箱账号
    msg['Cc'] = ",".join(cc_list) 
    msg['Subject'] = Header(subject, 'utf-8')     # 邮件的主题，也可以说是标题,'utf-8'

    text = MIMEText(content, 'plain', 'utf-8')
    msg.attach(text)
    
    # 可以多个附件 for循环
    f = open(address, 'rb')
    att1 = MIMEApplication(f.read())
    att1.add_header('Content-Disposition', 'attachment', filename=rename)
    msg.attach(att1)
·
    server = smtplib.SMTP_SSL("smtp.chinatelecom.cn", 465, timeout=30)
    server.login(my_sender, my_pass)
    server.sendmail(my_sender, receiver + cc_list, msg.as_string()) # cc_list  抄送


if __name__ == "__main__":
    # mail(['xxxx@qq.com'], u'步test', u'请查收', ["xxxxxr@163.com"])
    try:
        mail_file(['xxxx@qq.com'], u'主题', u'内容', u'C:\\余额对应.xlsx', ["qxxxxx@163.com"])
        print 'done!'
    except Exception as e:
        print 'fail'
    