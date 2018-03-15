#coding:utf-8
import poplib
import cStringIO
import email
import base64
import chardet
import time 
#pop3 get email

'''
1. 连接pop3服务器 (poplib.POP3.__init__)
2. 发送用户名和密码进行验证 (poplib.POP3.user poplib.POP3.pass_)
3. 获取邮箱中信件信息 (poplib.POP3.stat)
4. 收取邮件 (poplib.POP3.retr)
5. 删除邮件 (poplib.POP3.dele)
6. 退出 (poplib.POP3.quit)
'''

for t in range(1,100):
    print t

    M=poplib.POP3('pop3.163.com')
    M.user('xx@163.com')
    M.pass_('xxx')
    print M.stat()
    numMessages=len(M.list()[1])
    print 'num of messages',numMessages
    for i in range(1,numMessages+1):
        print u"正在读取第%s封邮件"%i
        m = M.retr(i)
        buf = cStringIO.StringIO()
        for j in m[1]:
            print >>buf,j
        buf.seek(0)
        #
        msg = email.message_from_file(buf)
        for part in msg.walk():
            contenttype = part.get_content_type()
            filename = part.get_filename()
            mycode=part.get_content_charset()
            if filename:  
                data = part.get_payload(decode=True)  
                h = email.Header.Header(filename)  
                dh = email.Header.decode_header(h)  
                fname = dh[0][0]  
                encodeStr = dh[0][1]  
                if encodeStr != None:  
                    fname = fname.decode(encodeStr, mycode)
                print fname
                #end if  
                f = open("mail%s%s"%(i,fname), 'wb')  
                f.write(data)  
                f.close()
    time.sleep(0.1)
