import smtplib,ssl
import sys
import os
import socket
from email.mime.base import MIMEBase 
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class send_emails:


    def __init__(self):
        self.sender_email=''
        self.receiver_email=''
        self.password=''
        #self.context_=''

    def user_input(self):
        self.sender_email="saayan@headrun.com"
        self.receiver_email=["saayan8981@gmail.com"]
        self.cc=["saayan9045@yahoo.com"]
        #self.bcc=["saayan9045@yahoo.com"]
        self.password="9891274567"

    def user_message(self):
        text="""Hi,
        
    How are you??



    this is system generated mail, so don't reply


    Thanks & regards,
    Saayan.       """

        return text    

    def main(self):
        self.user_input()
        #import pdb;pdb.set_trace()
        message=MIMEMultipart("alternative")
        message["Subject"]="Message from python!!"
        message["From"]=self.sender_email
        message["To"]=",".join([email_id for email_id in self.receiver_email])
        message['Cc']=",".join(self.cc)
        #message['Bcc']=",".join([email for email in self.bcc])
        port =25
        text=self.user_message()
        part1=MIMEText(text,"plain")

        message.attach(part1)
        #message.attach(part2)
        try:
            #self.context_=ssl.create_default_context()
            server = smtplib.SMTP("smtp.gmail.com",25)
            server.ehlo()
            server.starttls()
            server.login(self.sender_email,self.password)
            server.sendmail(self.sender_email,self.receiver_email+self.cc,message.as_string())
            server.quit()
            print("mail sent to %s"%self.receiver_email)
        except socket.error as e:
            print("retrying........",type(e))
            self.main()        

object_=send_emails()
object_.main()