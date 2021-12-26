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