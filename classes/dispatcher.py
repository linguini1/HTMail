# Dispatcher class to handle mailing list and sending of batch emails
__author__ = "Matteo Golin"

# Imports
import smtplib
import ssl
from .email import Email

# Constants
PORT: int = 465  # SSL port
CONTEXT = ssl.create_default_context()


# Class
class Dispatcher:

    """Creates secure connection for batch email dispatch."""

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def send_batch(self, email: Email, mailing_list: list[str]):

        """Sends emails in batch."""

        with smtplib.SMTP_SSL('smtp.gmail.com', PORT, context=CONTEXT) as server:
            server.login(self.username, self.password)

            for recipient in mailing_list:
                email.send(recipient, server)

            server.quit()
