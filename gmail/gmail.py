"""
please place a file gmail_settings.py with two varialbes:

GMAIL_ACCOUNT = ""
GMAIL_PASSWORD = ""

or set the environment variables

GMAIL_ACCOUNT = ""
GMAIL_PASSWORD = ""

"""


from settings import GMAIL_ACCOUNT, GMAIL_PASSWORD

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import os


class Gmail(object):
    def __init__(self,gmail_id = GMAIL_ACCOUNT, gmail_pwd = GMAIL_PASSWORD):
                
        self.gmail_id = gmail_id
        self.gmail_pwd = gmail_pwd
        
        self.gmail_server = smtplib.SMTP("smtp.gmail.com", 587)
        self.gmail_server.ehlo()
        self.gmail_server.starttls()
        self.gmail_server.ehlo()
        self.gmail_server.login(self.gmail_id, self.gmail_pwd)
    
    
    def disconnected(self):
        self.gmail_server.close()
        
        
    def create_new_message(self, subject = "[Gmail Notifier TEST] Sending mail TESTING", type = 'alternative'):
        if type == None:
            self.msg = MIMEMultipart()
        else:
            self.msg = MIMEMultipart(type)
        
        self.msg["From"] = self.gmail_id
        self.msg["Subject"] = subject
        
        
    def add_text_into_message(self, text = "Sending mail TESTING"):
        self.msg.attach(MIMEText(text,'plain'))
        

    def add_html_into_message(self, html = "<h1>Sending mail TESTING</h1>"):
        self.msg.attach(MIMEText(html,'html'))
        
        
    def attach_files_into_message(self, files_path_list = []):
        for attach in files_path_list:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(open(attach, 'rb').read())
            Encoders.encode_base64(part)
            part.add_header('Content-Disposition',
                            'attachment; filename="%s"' % os.path.basename(attach))
            self.msg.attach(part)
             
                
    def send_message(self, mail_to_list = ["c3h3.tw@gmail.com"], send_at_once=False):
        if send_at_once:
            self.gmail_server.sendmail(self.gmail_id, mail_to_list, self.msg.as_string())
        else:
            for to in mail_to_list:
                self.msg["To"] = to 
                self.gmail_server.sendmail(self.gmail_id, to, self.msg.as_string())
            
            
