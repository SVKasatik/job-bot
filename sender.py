# sender.py

import yagmail
from dotenv import load_dotenv
import os
load_dotenv()

SENDER_EMAIL = os.getenv("EMAIL")
APP_PASSWORD = os.getenv("PASSWORD")

def send_email(recipient, message, job):
    if not recipient:
        print(f"[SKIP] No recipient email for job: {job['title']} at {job['company']}")
        return

    subject = f"Bewerbung: {job['title']} bei {job['company']}"

    try:
        yag = yagmail.SMTP(SENDER_EMAIL, APP_PASSWORD)
        yag.send(
            to=recipient,
            subject=subject,
            contents=message
            # attachments=['cv.pdf']  # можешь раскомментировать при необходимости
        )
        print(f"[SENT] Application sent to {recipient} for {job['title']}")
    except Exception as e:
        print(f"[ERROR] Failed to send email: {e}")
