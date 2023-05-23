# https://github.com/ifrankandrade/automation
#qemtotejzhacmyaw
import smtplib
import ssl
from email.message import EmailMessage

# Define email sender and receiver
email_sender = 'bhpdjemaq2021@gmail.com'
email_password = 'upgodrzziajcqbjv'
email_receiver = 'ematevez@gmail.com'

# Set the subject and body of the email
subject = 'Check out your account!'
body = """
Se le ha enviado una solicitud: http://192.168.1.44:8000/dashboard/
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)
with open("djangochat/Auxiliar/PDF-Creator/Reporte.pdf", "rb") as f:
    em.add_attachment(
        f.read(),
        filename="Reporte.pdf",
        maintype="application",
        subtype="pdf"
    )
# Add SSL (layer of security)
context = ssl.create_default_context()

# Log in and send the email
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())