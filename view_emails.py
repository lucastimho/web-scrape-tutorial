import email
import imaplib
import getpass

M = imaplib.IMAP4_SSL("imap.gmail.com")
email_user = getpass.getpass("Enter email: ")
password = getpass.getpass("Enter password: ")
M.login(email_user, password)
print(M.list())
print(M.select("inbox"))
typ, data = M.search(None, 'Subject "New Test Python')
