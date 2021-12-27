# NUSSDS Mass E-Mail Bot

## Table of Contents
 <hr />

* [Description](#description)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Contact](#contact)

## Description
* Email Script that allows for users to place a pre-set html email template into "template.txt", followed by the string variables containing the emails and information of emails/organisations they wish to send to.
* Script will read the respective files, craft a message meant for that particular organisation and email, together with any attachment.

## Screenshots
* Email preview function that requires user confirmation before proceeding
  ![Email Preview Function](screenshots/email_preview.jpg?raw=true)
* Script will ask user for explicit confirmation(by typing 'YES' into python console) before the email execution is carried out
  ![Email Confirmation Function](screenshots/email_confirmation.png?raw=true)
* Script will also output string message that email has been sent successfully upon completion.
  ![Email Sent Function](screenshots/email_sent.jpg?raw=true)

## Setup
1. Clone this repository
2. Inside the src directory, create 3 other directories, naming them
   * attachments
   * email_list
   * email_script
3. In the 'attachments' directory, place all pdf documents that you wish to attach in the email
4. In the 'email_list' directory, create a .xlsx file named email_list.xlsx
5. In the 'email_script' directory, create a .txt file named template.txt and place the html version of the email content inside.

## Usage
* In order to use the script, proceed to open up 'config.toml' in IDE.
* Under the 'sender' dictionary, input your email details (address and password)
* NOTE: DO NOT COMMIT/PUSH THIS TO GITHUB for privacy reasons.
* Under the 'email_content' dictionary, put in your full name and the short name.

## Project Status
* This project is still being updated, and worked on, as of 27/12/2021.
* Currently still working on adding more features.

## Room for Improvement
* Security: Storing email address and password in environment variables instead of in config.toml.
* Time Complexity: Reduce operations by reducing the number of os.chdir calls within the for loop.

## Contact
* Do email me at aujunhui88@gmail.com if there are any queries or suggestions you have for me :)