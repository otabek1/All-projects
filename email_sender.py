import smtplib
from email.message import EmailMessage

email = EmailMessage()
email["from"] = "grand007hunter@gmail.com"
email["to"] = "abduraufov_otabek@mail.ru"

email.set_content("Hi there")

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("grand007hunter@gmail.com", "password")
    smtp.send_message(email)
    print("worked")