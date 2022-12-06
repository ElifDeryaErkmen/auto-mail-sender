import smtplib, ssl
from email.message import EmailMessage

msg = EmailMessage()
msg.set_content("The body of the email is here")
msg["Subject"] = "An Email Alert"
msg["From"] = "xx.xx@gmail.com"
msg["To"] = "walife7342@aikusy.com"

context=ssl.create_default_context()

with smtplib.SMTP("smtp.gmail.com", port=5687) as smtp:
    smtp.starttls(context=context)
    smtp.login(msg["From"], "passw0rd")
    smtp.send_message(msg)

