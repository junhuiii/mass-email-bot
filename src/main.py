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


# Function to create connection to localhost for testing purposes
# For windows: open cmd and input <py -m smtpd -c DebuggingServer -n localhost:1025>
# For MacOS: open terminal and input <python3 -m smtpd -c DebuggingServer -n localhost:1025>
# For testing purpose, EMAIL_ADDRESS AND receiver can be blank strings
def debug_local_server(subject, body):
    test_email = ""
    receiver = ""
    with smtplib.SMTP('localhost', 1025) as smtp:
        msg = f'Subject: {subject}\n\n{body}'
        smtp.sendmail(test_email, receiver, msg)


# Function to log into gmail account
def login_email(email, pw, server):
    with smtplib.SMTP_SSL(server, 465) as smtp:
        smtp.login(email, pw)
    print(f'Login to {email} successful.')


# Function to change directories
def change_directory(extension):
    cwd = os.getcwd()
    os.chdir(cwd + extension)


# Function to list files in a directory
def list_files(path):
    files = os.listdir(path)
    return files


# TODO: Function to read attachments before attaching to email message
def read_files(lst):
    for file in lst:
        with open(file, 'rb') as f:
            file_data = f.read()
            file_name = f.name
    return file_data, file_name

# TODO: Function to get list of email receivers to send to from config.toml


# Function to print email message in Intellij for checking purposes
def print_email(msg_obj):
    print(str(msg_obj))


if __name__ == '__main__':
    # Read config.toml
    test_config = read_config('config.toml')

    # Obtain login details from config.toml
    email_address = test_config['sender']['email_address']
    email_password = test_config['sender']['password']
    email_server = test_config['sender']['server']
    # login_email(email_address,email_password,email_server) # Uncomment when details have been added to config.toml

    # Draft message
    msg = EmailMessage()
    msg["Subject"] = " "
    msg["From"] = " "
    msg["To"] = " "
    msg.set_content(" ")

    # Navigate to attachment directory
    attachment_directory = test_config["directories"]["attachments"]
    change_directory(attachment_directory)

    # List attachments in attachment directory
    attachments = list_files(os.getcwd())

    # Attach attachments to msg
    f_data, f_name = read_files(attachments)

    # Uncomment when reading to send
    # msg.add_attachment(f_data, maintype='application', subtype='octet-stream', filename=f_name)







