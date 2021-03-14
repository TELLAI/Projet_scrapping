import smtplib, ssl 
from email.mime.text import MIMEText
from email import encoders
from mail_mysql import Week_foot
import os
from dotenv import load_dotenv
load_dotenv()

test = Week_foot()
test.equipe()
data = test.data
sms = "***"
mdp= os.environ.get("my_mdp")
email= os.environ.get("my_email")
for i in data:
    for y in i:
        sms = sms + y + " * "
    sms = sms + " *** "
msg = MIMEText(sms, 'html')
msg['From'] = 'tellaiyt@gmail.com'
msg['To'] = 'tellaiyt@gmail.com'
msg['Subject'] = 'Le sujet de mon mail' 
s = smtplib.SMTP_SSL(host = 'smtp.gmail.com', port = 465)
s.login(user = email, password = mdp)
s.sendmail(email, email, msg.as_string())
s.quit()