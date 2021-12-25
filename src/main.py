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
        message = f'Subject: {subject}\n\n{body}'
        smtp.sendmail(test_email, receiver, message)


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
def save_to_html(html_str):
    file = open("template.html", "w")
    file.write(html_str)
    file.close()


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
    email_template = list_files(os.getcwd())  # List files in email_script directory

    # Dictionary to test replacement of variables
    replacements = {'organisation_name': 'csgodyune'}

    # Set short_name and full_name variable from config.toml file
    for var, name in config_file['email_content'].items():
        replacements[var] = name

    # TODO: Add try-catch to handle case where "template.txt" doesn't exist
    if len(email_template) == 2 and "template.txt" in email_template:  # Check for existence of "template.txt"
        with open(email_template[email_template.index("template.txt")], mode='r', encoding='utf-8-sig') as fle:
            html_string = fle.read().format(**replacements)  # read template.txt as string

    msg.set_content(html_string, subtype='html')  # convert to html and attach to msg object
    save_to_html(html_string)  # update to "template.html"
    webbrowser.get('windows-default').open_new("template.html")  # open in default browser
    # Request for user to check email
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
