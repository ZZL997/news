import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(from_addr, password, to_addr, subject, body, smtp_server='smtp.163.com', smtp_port=25):
    """发送邮件函数

    Args:
        from_addr (str): 发件人邮箱地址
        password (str): 发件人邮箱密码
        to_addr (str): 收件人邮箱地址
        subject (str): 邮件主题
        body (str): 邮件正文
        smtp_server (str, optional): SMTP 服务器地址。默认为 'smtp.gmail.com'。
        smtp_port (int, optional): SMTP 服务器端口号。默认为 587。

    Raises:
        ValueError: 如果收件人地址或发件人地址未设置，则抛出 ValueError。

    """
    # 如果收件人地址或发件人地址未设置，则抛出 ValueError
    if not from_addr or not password:
        raise ValueError('发件人邮箱或密码未设置')

    # 创建邮件对象
    msg = MIMEMultipart()

    # 设置邮件头部信息
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = subject

    # 添加邮件正文
    msg.attach(MIMEText(body, 'plain'))

    # 连接邮件服务器
    smtp_obj = smtplib.SMTP(smtp_server, smtp_port)

    # 开始 TLS 加密
    smtp_obj.starttls()

    # 登录邮箱
    smtp_obj.login(from_addr, password)

    # 发送邮件
    smtp_obj.sendmail(from_addr, [to_addr], msg.as_string())

    # 关闭连接
    smtp_obj.quit()



from_addr = 'zlg769479802@163.com'
password = 'ZCUIUNTTBEYFXZPI'
to_addr = '2327433383@qq.com'
subject = 'Test Email'
body = 'This is a test email.'

send_email(from_addr, password, to_addr, subject, body)
