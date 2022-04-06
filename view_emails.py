import email
import imaplib
import getpass
from unittest import result

M = imaplib.IMAP4_SSL("imap.gmail.com")
email_user = getpass.getpass("Enter email: ")
password = getpass.getpass("Enter password: ")
M.login(email_user, password)
print(M.list())
print(M.select("inbox"))
typ, data = M.search(None, 'Subject "New Test Python')
email_id = data[0]
result_data, email_data = M.fetch(email_id, '{RFC822}')
raw_email = email_data[0][1]
raw_email_string = raw_email.decode("utf-8")
email_message = email.message_from_string(raw_email_string)
for part in email_message.walk():
    if part.get_content_type() == "text/plain":
        body = part.get_payload(decode=True)
        print(body)
