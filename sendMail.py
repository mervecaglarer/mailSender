import requests
import json
from string import Template
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import csv


emails=[]
names=[]
urls=[]
with open('mailaddress.csv', encoding='utf-8') as csv_file: # csv file has mail addresses which are wanted to send mail
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        emails.append(row[1])
        names.append(row[0])

def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

s = smtplib.SMTP(host='smtp.gmail.com', port=587)
s.starttls()
s.login('sendermail@gmail.com', 'password') # sender mail address and password 

message_template = read_template('examplemail.txt') # txt file has mail which are wanted to send 
cc=['ccmail@gmail.com'] # cc mail address

# For each contact, send the email:
for email in emails:

    msg = MIMEMultipart() # create a message
    message = message_template.substitute()

    msg['From'] = 'sendermail@gmail.com'
    msg['To'] = email
    msg['Subject'] = "Subject" # subject what you want
    msg.add_header("Cc", ", ".join(cc))
    
    # add in the message body
    msg.attach(MIMEText(message, 'plain'))
    
    # send the message via the server set up earlier.
    s.send_message(msg)
    del msg