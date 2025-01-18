import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

# nfczjkduazlobdfi
# ### 1.邮件内容配置 ###
msg = MIMEText("测试", 'html', 'utf-8')
msg['From'] = formataddr(["Ask锟", "815661337@qq.com"])
msg['Subject'] = "你好"

# ### 2.发送邮件 ###
server = smtplib.SMTP_SSL("smtp.qq.com")
server.login("815661337@qq.com", "nfczjkduazlobdfi")
server.sendmail("815661337@qq.com", "815661337@qq.com", msg.as_string())
server.quit()