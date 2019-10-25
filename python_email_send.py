import smtplib,ssl
import sys
import os
import socket
import ntpath
import datetime
from email.mime.base import MIMEBase 
from email import Encoders
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
        
    Please find the attachments below.




    This is system generated mail, so don't reply.


    Thanks & regards,
    Saayan.       """

        return text  


    def read_attachment(self,attachment_):
        #import pdb;pdb.set_trace()
        with open(attachment_, "rb") as attachment:
            # Add file as application/octet-stream
            # Email client can usually download this automatically as attachment
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
            # Encode file in ASCII characters to send by email    
            Encoders.encode_base64(part)

            # Add header as key/value pair to attachment part
            part.add_header(
                "Content-Disposition",
                "attachment", filename=ntpath.basename(attachment_)) 
 
            return part     

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
        filenames=['holiday_list_caavo.csv','amazon_netflix.xlsx']
        for file in filenames:
            attachment=os.getcwd()+'/attachments/'+file
            file_=self.read_attachment(attachment)
            message.attach(file_)
        try:
            #self.context_=ssl.create_default_context()
            server = smtplib.SMTP("smtp.gmail.com",25)
            server.ehlo()
            server.starttls()
            server.login(self.sender_email,self.password)
            server.sendmail(self.sender_email,self.receiver_email+self.cc,message.as_string())
            server.quit()
            print("mail sent to %s %s"%(",".join(self.receiver_email+self.cc),datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        except socket.error as e:
            print("retrying........",type(e))
            self.main()        

object_=send_emails()
object_.main()