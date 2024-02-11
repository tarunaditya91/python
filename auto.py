from email.message import EmailMessage

import ssl
import smtplib

email_sender = 'shankertarunaditya369@gmail.com'
email_password='swwm eiml rlhe gazf'

email_receiver = 'tarunaditya91@gmail.com'

subject="testing to send a auto email"

body="""
where are you
"""

em=EmailMessage()
em['From']=email_sender
em['To']=email_receiver
em['Subject']=subject
em.set_content(body)

context=ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_receiver,em.as_string())


