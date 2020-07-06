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
with open('filename.csv',encoding='utf-8') as csv_file:
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
s.login('example@gmail.com', 'password')

message_template = read_template('examplemail.txt')
cc=['example@gmail.com']
# For each contact, send the email:
for email in emails:
    msg = MIMEMultipart()       # create a message

    message = message_template.substitute()

    msg['From']='example@gmail.com'
    msg['To']=email
    msg['Subject']="Subject"
    msg.add_header("Cc", ", ".join(cc))
    
    # add in the message body
    msg.attach(MIMEText(message, 'plain'))
    
    # send the message via the server set up earlier.
    s.send_message(msg)
    del msg