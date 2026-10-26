import smtplib
from email.message import EmailMessage
msg = EmailMessage()
msg['Subject'] = 'Test mail'
msg['From'] = 'you@gmail.com'
msg['To'] = 'recipient@gmail.com'
msg.set_content('Hello from Python')
with smtplib.SMTP('smtp.gmail.com', 587) as s:
 s.starttls()
 s.login('username', 'password')
 s.send_message(msg)