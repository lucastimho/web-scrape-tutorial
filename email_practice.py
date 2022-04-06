import email
from email import message
import smtplib
import getpass

# if 587 doesn't work use 465 or nothing
smtp_object = smtplib.SMTP("smtp.gmail.com", 587)
print(smtp_object.ehlo())
print(smtp_object.starttls())
email_user = getpass.getpass("Email: ")
password = getpass.getpass("Password: ")
smtp_object.login(email_user, password)
from_address = email_user
to_address = email_user
subject = input("enter subject line here: ")
message_send = input("enter the body message here: ")
msg = "Subject: " + subject + "\n" + message_send
smtp_object.send_message(from_address, to_address, msg)
smtp_object.quit()
