import smtplib
from email.mime.text import MIMEText
from config import *


def send_mail(title, text):
    print("Sending an email to %s" % ", ".join(TO))
    message = MIMEText(text, "plain", "utf8")
    message["Subject"] = title
    message["From"] = FROM
    message["To"] = ", ".join(TO)

    smtp = None
    if SMTP_SSL:
        smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
    else:
        smtp = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)

    if SMTP_TTL:
        smtp.starttls()
    smtp.login(SMTP_USER, SMTP_PASSWORD)

    smtp.sendmail(message["From"], TO, message.as_string())
    smtp.quit()