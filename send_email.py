import smtplib 
from email.mime.text import MIMEText
from email.header import Header

mailhost='smtp.qq.com'
qqmail = smtplib.SMTP_SSL(mailhost,465)

account = input('请输入你的邮箱：')
password = input('请输入你的密码：')
#不是账号密码，是登录第三方客户端邮箱的授权码
qqmail.login(account,password)

receiver=input('请输入收件人的邮箱：')

content=input('请输入邮件正文：')
message = MIMEText(content, 'plain', 'utf-8')
#实例化一个MIMEText邮件对象，该对象需要写进三个参数，分别是邮件正文，文本格式和编码
subject = input('请输入你的邮件主题：')
message['From'] = Header(account)
message['To'] = Header(receiver)
message['Subject'] = Header(subject, 'utf-8')

try:
    qqmail.sendmail(account, receiver, message.as_string())
    print ('邮件发送成功')
except:
    print ('邮件发送失败')
qqmail.quit()