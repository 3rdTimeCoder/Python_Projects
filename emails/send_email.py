from email.message import EmailMessage
import config
import ssl
import smtplib

email_sender = config.EMAIL
email_password = config.EMAIL_PASSWORD

email_reciever = config.EMAIL_RECIEVER

subject = "This is a test"
body = "This is an email to test the app's functionality"

# setup email instance
email = EmailMessage()
email['From'] = f"The Fourth <{email_sender}>"
email['To'] = email_reciever
email['subject'] = subject
email.set_content(body)

# context
context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_reciever, email.as_string())





