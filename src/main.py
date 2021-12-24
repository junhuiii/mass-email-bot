import pytoml
import smtplib
import os
from email.message import EmailMessage
import webbrowser
import sys

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


# Function to change directories
def change_directory(current, extension):
    os.chdir(current + extension)


# Function to list files in a directory
def list_files(path):
    files = os.listdir(path)
    return files


# Function to read attachments before attaching to email message
def read_files(lst):
    for file in lst:
        with open(file, 'rb') as f:
            file_data = f.read()
            file_name = f.name
    return file_data, file_name

# TODO: Function to get list of email receivers to send to from config.toml


# TODO: Work on function to print email body in python console for user to check through before sending
def save_to_html(html_string):
    file = open("template.html", "w")
    file.write(html_string)
    file.close()


# Function to print email message in Intellij for checking purposes
def print_email(msg_obj):
    print(str(msg_obj))


if __name__ == '__main__':
    # Read config.toml
    config_file = read_config('config.toml')

    # Store cwd for future use
    base_cwd = os.getcwd()

    # Obtain login details from config.toml
    email_address = config_file['sender']['email_address']
    email_password = config_file['sender']['password']
    email_server = config_file['sender']['server']

    # Draft message
    msg = EmailMessage()
    msg["Subject"] = "test 1"
    msg["From"] = email_address
    msg["To"] = email_address

    # Navigate to email_script directory
    email_script_directory = config_file["directories"]["email_script"]
    change_directory(base_cwd, email_script_directory)
    email_template = list_files(os.getcwd())
    if len(email_template) == 2 and "template.txt" in email_template:
        with open(email_template[email_template.index("template.txt")], mode='r', encoding='utf-8-sig') as f:
            test_str = f.read()
    msg.set_content(test_str, subtype='html')
    save_to_html(test_str)
    webbrowser.get('windows-default').open_new("template.html")
    check_preview = input("Please check preview of email and choose whether to proceed (YES/NO): ")
    if check_preview != "YES":
        print("Stopping program...")
        sys.exit()

    # Navigate to attachment directory
    attachment_directory = config_file["directories"]["attachments"]
    change_directory(base_cwd, attachment_directory)

    # List attachments in attachment directory
    attachments = list_files(os.getcwd())

    # Attach attachments to msg
    f_data, f_name = read_files(attachments)

    # Uncomment when reading to send
    msg.add_attachment(f_data, maintype='application', subtype='octet-stream', filename=f_name)
    # Uncomment when ready to send email
    # with smtplib.SMTP_SSL(email_server, 465) as smtp:
    #     smtp.login(email_address, email_password)
    #     smtp.send_message(msg)
    #     print(f'Email sent to {email_address} successful.')
