import pytoml
import smtplib
import os
from email.message import EmailMessage

# Final Variables
CONFIG_PATH = 'config.toml'


# Function to import from config.toml, which contains environment variables
def read_config(path):
    config = pytoml.load(open(path, 'rb'))
    return config

# TODO: Function to create SMTP connection to gmail account (Use SSL Class)


# TODO: Function to create connection to localhost for testing purposes
# For windows: open cmd and input <py -m smtpd -c DebuggingServer -n localhost:1025>
# For MacOS: open terminal and input <python3 -m smtpd -c DebuggingServer -n localhost:1025>
# For testing purpose, EMAIL_ADDRESS AND receiver can be blank strings
def debug_local_server(subject, body):
    test_email = ""
    receiver = ""
    with smtplib.SMTP('localhost', 1025) as smtp:
        msg = f'Subject: {subject}\n\n{body}'
        smtp.sendmail(test_email, receiver, msg)

# TODO: Function to log into gmail account

# TODO: Function to open documents in attachments directory

# TODO: Function to add attachment to email before sending

# TODO: Function to get list of email receivers to send to from config.toml

if __name__ == '__main__':
    print("Hello World!")
