# Email object to be sent
__author__ = "Matteo Golin"

# Imports
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from .html import HTMLObject


# Classes
class Email:

    """Email object to be sent."""

    def __init__(self, subject: str, text: str = None, html: HTMLObject = None):

        # Message creation
        self.message = MIMEMultipart('alternative')
        self.message["Subject"] = subject

        # Attaching parts
        if text:
            plaintext = MIMEText(text, 'plain')
            self.message.attach(plaintext)

        if html:
            HTML = MIMEText(html.html_string, 'html')
            self.message.attach(HTML)

    def send(self, recipient: str, server: smtplib.SMTP_SSL) -> None:

        """Sends the email to the recipient."""

        self.message["To"] = recipient
        self.message["From"] = server.user

        server.sendmail(server.user, recipient, self.message.as_string())
