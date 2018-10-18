import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
username = "showsreminderinnovaccer"
password = "innovaccer1@"
fromemail = "showsreminderinnovaccer@gmail.com"

def sendemail(email, msg1):
    smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()
    smtpserver.login(username, password)
    msg = MIMEMultipart()
    msg['From'] = fromemail
    msg['To'] = email
    msg['Subject'] = "Reminder about your favourite shows"
    msg.attach(MIMEText(msg1,'plain'))
    text = msg.as_string()
    smtpserver.sendmail(fromemail, email, text)
