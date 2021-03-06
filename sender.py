import smtplib, ssl 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
import os
from dotenv import load_dotenv

# if os.environ.get("my_ENV") != "production":
load_dotenv()

def send_mail(result, email_to):
    sms = result
    mdp= os.environ.get("SENDER_PWD")
    email= os.environ.get("SENDER_MAIL")
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = email_to
    msg['Subject'] = 'user list sender' 
    s = smtplib.SMTP(host = 'smtp.gmail.com', port=587)
    s.starttls()
    s.login(user = email, password = mdp)
    msg.attach(MIMEText(sms, 'html'))
    s.send_message(msg)


# import smtplib, ssl 
# from email.mime.text import MIMEText
# from email import encoders
# import os
# from dotenv import load_dotenv
# load_dotenv()

# def send_mail(email_to):
#     sms = "test"
#     # sms = "***"
#     pwd= os.environ.get("SENDER_PWD")
#     email= os.environ.get("SENDER_MAIL")
#     # for i in data:
#     #     for y in i:
#     #         sms = sms + y + " * "
#     #     sms = sms + " *** "
#     msg = MIMEText(sms, 'html')
#     msg['From'] = email
#     msg['To'] = email_to
#     msg['Subject'] = 'bonjour !!!' 
#     s = smtplib.SMTP_SSL(host = 'smtp.gmail.com', port = 465)
#     s.starttls()
#     s.login(user = email, password = pwd)
#     s.sendmail(email, email, msg.as_string())
#     s.quit()
