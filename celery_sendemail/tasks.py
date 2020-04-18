# 装饰器从所有可调用对象中创建任务类
from celery_sendemail.celery import app
from django.core.mail import send_mail

from blogproject.settings import EMAIL_FROM


@app.task
def sendemail():
        email=''
        title = 'Announcing the go-filecoin alphanet'
        body="""
        
        """
        ##发送邮件
        """
        subject, message, from_email, recipient_list,
              fail_silently=False, auth_user=None, auth_password=None,
              connection=None, html_message=None
        主题 ，信息，发件人，收件人列表
        """
        send_status=send_mail(title,body,EMAIL_FROM,[email,])
        if send_status:
            print('send  successful')