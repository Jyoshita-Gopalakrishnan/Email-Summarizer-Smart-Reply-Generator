# modules/email_parser.py
from email import message_from_string

def parse_email(raw_email: str) -> dict:
    msg = message_from_string(raw_email)
    subject = msg.get("Subject", "")
    sender = msg.get("From", "")
    body = ""

    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                body += part.get_payload(decode=True).decode()
    else:
        body = msg.get_payload(decode=True).decode()

    return {
        "subject": subject,
        "sender": sender,
        "body": body
    }
