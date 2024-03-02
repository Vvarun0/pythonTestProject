import subprocess
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Run Robot Framework test cases
subprocess.run(["robot", "path/to/your/test/suite"])

# Get the results file
results_file = "path/to/results_file.xml"

# Read the results file
with open(results_file, "r") as file:
    results = file.read()

# Set up email parameters
from_email = "your_email@gmail.com"
to_email = "recipient_email@gmail.com"
subject = "Robot Framework Test Results"
body = results

# Send the email
msg = MIMEMultipart()
msg["From"] = from_email
msg["To"] = to_email
msg["Subject"] = subject
msg.attach(MIMEText(body, "plain"))

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(from_email, "your_password")
server.send_message(msg)
server.quit()