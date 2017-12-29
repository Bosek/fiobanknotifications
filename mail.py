import smtplib
from secrets import *

from email.mime.text import MIMEText

def send_mail(title, text):
    message = MIMEText(text, 'plain', 'utf8')
    message['Subject'] = title
    message['From'] = FROM
    message['To'] = ", ".join(TO)

    smtp = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    smtp.starttls()
    smtp.login(SMTP_USER, SMTP_PASSWORD)

    smtp.sendmail(message['From'], TO, message.as_string())
    smtp.quit()