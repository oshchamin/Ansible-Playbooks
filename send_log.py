# Written by Oshan chamika
# Date: 2024-12-21
# This script sends an email with an attached log file using Python's smtplib library.

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Email configuration
sender_email = "xylemexcelsior@gmail.com"
receiver_email = ["oshand@ts.lk", "vimukthi@tspl.com"]
password = "rcrcfodhpanfgolb" 
subject = "Server Log File from OpsLink"

# File to send
log_file = "/home/opslink/opslink.log"

# Create email message
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = ", ".join(receiver_email)
message["Subject"] = subject

# Email body
body = """
OpsLink Team,

Please find the attached OpsLink server log file for your reference.

Keywords for the search error:
- fatal
- failed
- unreachable
- dependency

Note: A fresh installation will create an error of backing up the osupdate.txt file due to the lack of a previous txt file.

If you have any questions, please feel free to reach out.

Best regards,
Oshan Dissanyake
Email: oshand@ts.lk
OpsLink Team,
TS Technologies.
"""
message.attach(MIMEText(body, "plain"))

# Attach the log file
with open(log_file, "rb") as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Encode the file in ASCII characters to send by email    
encoders.encode_base64(part)
part.add_header(
    "Content-Disposition",
    f"attachment; filename={log_file.split('/')[-1]}",
)
message.attach(part)

# Send the email
try:
    with smtplib.SMTP("smtp.gmail.com", 587) as server:  # Replace with your SMTP server
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
    print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")
