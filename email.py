import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path 

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'user name'
email['to'] = '<to email adress>'
email['subject'] = 'you won 10,00,000 dollars!'

email.set_content(html.substitute|({'name':'TinTin'}),'html')

with smtplib.SMTP(host='smtp.gmail.com',port=587)
as smtp:
	smtp.ehlo()
	smtp.startls()
	smtp.login('<your email adress>','<your password>')
	smtp.send_message(email)
	print('all good boss!')