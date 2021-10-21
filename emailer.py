import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.environ.get("email")
PASSWORD = os.environ.get("password")

class Emailer:
    def __init__(self):
        self.connection = smtplib.SMTP('smtp.gmail.com')
        self.connection.starttls()
        self.connection.login(user=EMAIL, password=PASSWORD)

    def send_mail(self, name, email, message):
        self.connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f'Subject: New Blog Message\n\nName: {name}\n\nEmail: {email}\n\n {message}'
        )
        self.connection.close()