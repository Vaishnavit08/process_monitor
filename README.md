# process_monitor
This Python script logs details of all currently running processes on the system at regular intervals and sends the log file via email. The script uses various modules like psutil for process information, smtplib for email functionality, and schedule for task scheduling.

Features:
Process Logging: Logs details including process ID, name, username, and virtual memory size.
Email Notification: Sends the generated log file to a specified email address.
Internet Check: Verifies internet connectivity before attempting to send the email.
Scheduler: Allows the user to specify the interval (in minutes) for log creation and email notification.


Usage:
Dependencies: Ensure the following Python packages are installed: psutil, schedule.
Run the Script: Execute the script with the desired interval (in minutes) as a command-line argument.
Example:  python main.py 5


Note:
Update the fromaddr and toaddr in the MailSender function with your actual email addresses.
Ensure that less secure app access is enabled for the Gmail account used to send emails.


Author: Vaishnavi Pravin Talekar
