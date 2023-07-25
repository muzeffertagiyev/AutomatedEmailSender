from datetime import date
import requests


class EmailData:
  
    def __init__(self):
        response = requests.get(url='https://api.npoint.io/de5d')
        self.email_data = response.json()
        self.emails = [email for index, email in enumerate(self.email_data['emails'])] 
        self.content = self.email_data['content']
        self.sender_email = self.email_data['sender_email']['email']
        self.sender_password = self.email_data['sender_email']['password']
        self.today = date.today().strftime("%d %B %Y")
        self.subject = self.email_data['subject'].replace('[DATE]',self.today)
