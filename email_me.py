# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 19:44:11 2019

@author: evans
"""
# Import smtplib for the actual sending function
import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(filename):
    port = 465  # For SSL
    context = ssl.create_default_context()
    
    
    #password = input("Type your password and press enter: ")
    password = "L33tChessK1ng!"
    # Create a secure SSL context
    
    sender_email = "sender+guyesutcliffe@gmail.com"
    receiver_email = "evansutcliffe@gmail.com"
    message = MIMEMultipart("alternative")
    message["Subject"] = "temperature data"
    message["From"] = sender_email
    message["To"] = receiver_email
    
    # Create a HTML version of your message
    body = """\
    <html>
      <body>
        <p>Log of Temperture data (see attached .txt file).<br><br>
           Cheers,<br>
           Evan<br>
        </p>
      </body>
    </html>
    """
    
    # Turn these into plain/html MIMEText objects
    message.attach(MIMEText(body, "html"))
    

    with open(filename, "rb") as attachment:      # In same directory as script
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
    
    # Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)
    
    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )
    
    # Add attachment to message and convert message to string
    message.attach(part)
    
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("guyesutcliffe@gmail.com", password)
        print("successfully logged in")
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("sent")


