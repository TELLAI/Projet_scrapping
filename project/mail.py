import smtplib, ssl 
from email.mime.text import MIMEText
from email import encoders
from mail_mysql import Week_foot

test = Week_foot()
test.equipe()
data = test.data
sms = "***"
for i in data:
    for y in i:
        sms = sms + y + " * "
    sms = sms + " *** "
msg = MIMEText(sms, 'html')
msg['From'] = 'tellaiyt@gmail.com'
msg['To'] = 'tellaiyt@gmail.com'
msg['Subject'] = 'Le sujet de mon mail' 
s = smtplib.SMTP_SSL(host = 'smtp.gmail.com', port = 465)
s.login(user = 'tellaiyt@gmail.com', password = 'Satellite93@')
s.sendmail('tellaiyt@gmail.com', 'tellaiyt@gmail.com', msg.as_string())
s.quit()