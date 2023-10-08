import smtplib
from .constantsHelper import settings
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def smtp_connect(msg):
    try:
        smtp_params = {
            "smtp": settings.SMTP_HOST,
            "mail": settings.SMTP_USER,
            "nombre": settings.SMTP_FROM_NAME,
            "puerto": settings.SMTP_PORT,
            "password": settings.SMTP_PASSWORD
        }
        smt_obj = smtplib.SMTP(smtp_params['smtp'])
        smt_obj.ehlo()
        smt_obj.starttls()
        smt_obj.login(smtp_params["mail"], smtp_params["password"])
        destinatario = msg['To'].split(', ') + msg['Cc'].split(', ')
        smt_obj.sendmail(smtp_params["mail"], destinatario, msg.as_string())
        smt_obj.quit()

        return True
    except Exception as e:
        print(e)
        return False
    
def send_mail(email: str, subject: str, body, text: str, cc: str = None) -> bool:
    try:
        msg = MIMEMultipart('alternativo')
        msg['From'] = settings.EMAILS_FROM_EMAIL
        msg['To'] = str(email).lower()
        msg['Cc'] = ', ' . join(cc if cc is not None else [])
        msg['Subject'] = subject
        msg['content-type'] = 'text/html; charset=utf-8'

        part = MIMEText(text, 'plain')
        part1 = MIMEText(body, 'html')

        msg.attach(part)
        msg.attach(part1)

        sent = smtp_connect(msg)
        if sent:
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False