import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from email_data import EmailData


class EmailService:
    email_data = EmailData()
    def send_email(self,files):
            with smtplib.SMTP(host='smtp.gmail.com',port=587) as connection:
                subject = self.email_data.subject
                connection.starttls()
                connection.login(user=self.email_data.sender_email,password=self.email_data.sender_password)
                
                for email in self.email_data.emails:
                    message = MIMEMultipart()
                    message['From'] = self.email_data.sender_email
                    message['To'] = email
                    message['Subject'] = subject
                    message_content = f'{self.email_data.content.replace("[NAME]",self.email_data.email_data["emails"][email]["name"].title()).replace("[DATE]",self.email_data.today)}'
                    message.attach(MIMEText(message_content))
                    for file in files:     
                        message.attach(file)
                    connection.sendmail(from_addr=self.email_data.sender_email, to_addrs=email, msg=message.as_string())

