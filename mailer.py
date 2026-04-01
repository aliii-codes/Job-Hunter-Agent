import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()

SENDER = os.getenv("EMAIL")
PASSWORD = os.getenv("EMAIL_APP_PASSWORD")
RECEIVER = os.getenv("EMAIL")  

def build_email(jobs):
    if not jobs:
        return "No matching jobs found today. Check back tomorrow!"

    body = "Today's Job Matches for Ali\n"
    body += "=" * 40 + "\n\n"

    for i, job in enumerate(jobs, 1):
        body += f"{i}. {job['title']} @ {job['company']}\n"
        body += f"   Why: {job['reason']}\n"
        body += f"   Link: {job['url']}\n"
        body += "\n"

    body += "=" * 40 + "\n"
    body += "Sent by your Job Hunter Agent | Munaf Studios\n"

    return body

def send_email(jobs):
    body = build_email(jobs)

    msg = MIMEMultipart()
    msg["From"] = SENDER
    msg["To"] = RECEIVER
    msg["Subject"] = f"{len(jobs)} Job Matches Today!"

    msg.attach(MIMEText(body, "plain"))

    try:
        mail = smtplib.SMTP("smtp.gmail.com", 587)
        mail.ehlo()
        mail.starttls()
        mail.login(SENDER, PASSWORD)
        mail.sendmail(SENDER, RECEIVER, msg.as_string())
        mail.close()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Email error: {e}")
