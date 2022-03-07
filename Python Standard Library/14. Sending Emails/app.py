from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
import smtplib


message = MIMEMultipart()
message["from"] = "test"
message["to"] = "test@gmail.com"
message["subject"] = "This is a test"
message.attach(MIMEText("Body", "plain"))
message.attach(MIMEImage(Path("test.png").read_bytes))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()  # transport layer security
    smtp.login("address", "password")
    smtp.send_message(message)
    print("Sent...")
